#!/usr/bin/env python3
# Copyright 2022 Canonical Ltd.
# See LICENSE file for licensing details.

"""Contains integration tests for the mysql-bundle."""

import logging

import pytest
from pytest_operator.plugin import OpsTest

from tests.integration.constants import APPLICATION_APP, MYSQL_APP, ROUTER_APP, TLS_APP

logger = logging.getLogger(__name__)


@pytest.mark.abort_on_fail
async def test_deploy_bundle(ops_test: OpsTest) -> None:
    """Deploy bundle with app and release as a product."""
    async with ops_test.fast_forward():
        logger.info(f"Deploying test app {APPLICATION_APP}")
        await ops_test.model.deploy(
            APPLICATION_APP,
            channel="edge",
            application_name=APPLICATION_APP,
            series="jammy",
            num_units=3,
        )

        logger.info(f"Deploying bundle: {MYSQL_APP}, {ROUTER_APP} and {TLS_APP}")
        await ops_test.model.deploy("./releases/latest/mysql-bundle.yaml")

        logger.info(f"Waiting for {MYSQL_APP} up and running...")
        await ops_test.model.wait_for_idle(
            apps=[MYSQL_APP],
            status="active",
            raise_on_blocked=True,
            timeout=15 * 60,
        )

        logger.info(f"Relate {APPLICATION_APP} with {ROUTER_APP}")
        await ops_test.model.relate(f"{APPLICATION_APP}", f"{ROUTER_APP}")

        logger.info("Waiting for all applications up and running...")
        await ops_test.model.wait_for_idle(
            apps=[MYSQL_APP, ROUTER_APP, TLS_APP, APPLICATION_APP],
            status="active",
            timeout=15 * 60,
        )
