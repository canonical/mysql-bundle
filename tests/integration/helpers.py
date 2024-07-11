# Copyright 2024 Canonical Ltd.
# See LICENSE file for licensing details.

from typing import Dict

from juju.unit import Unit
from pytest_operator.plugin import OpsTest


async def get_unit_ip(ops_test: OpsTest, unit_name: str) -> str:
    """Wrapper for getting unit ip.

    Args:
        ops_test: The ops test object passed into every test case
        unit_name: The name of the unit to get the address
    Returns:
        The (str) ip of the unit
    """
    return_code, stdout, _ = await ops_test.juju("ssh", unit_name, "ip", "route")

    assert return_code == 0

    # Example output line of ip route:
    # default via 10.0.143.1 dev eth0 proto dhcp src 10.0.143.225 metric 100
    for line in stdout.split("\n"):
        items = line.split()
        if items[0] == "default":
            return items[8]

    raise Exception("Unable to find the default entry in output of 'ip route'")


async def get_credentials(unit: Unit, username: str) -> Dict:
    """Helper to run an action to retrieve server config credentials.

    Args:
        unit: The juju unit on which to run the get-password action for server-config credentials

    Returns:
        A dictionary with the server config username and password
    """
    action = await unit.run_action(action_name="get-password", username=username)
    result = await action.wait()
    return result.results
