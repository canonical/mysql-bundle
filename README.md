# Canonical Distribution of MySQL + MySQLRouter
[![Charmhub](https://charmhub.io/mysql-bundle/badge.svg)](https://charmhub.io/mysql-bundle)
[![Release](https://github.com/canonical/mysql-bundle/actions/workflows/release.yaml/badge.svg)](https://github.com/canonical/mysql-bundle/actions/workflows/release.yaml)
[![Tests](https://github.com/canonical/mysql-bundle/actions/workflows/ci.yaml/badge.svg?branch=main)](https://github.com/canonical/mysql-bundle/actions/workflows/ci.yaml)

Welcome to the Canonical Distribution of MySQL + MySQLRouter.

The objective of this page is to provide directions to get up and running with Canonical MySQL charms.

## Installation

Currently, we support this distribution with Ubuntu 20.04.

To deploy the bundle to a bootstrapped juju controller, simply run

```shell
juju deploy mysql-bundle
```

## Bundle Components
- [mysql](https://charmhub.io/mysql): a machine charm to deploy MySQL with Group Replication.
- [mysql-router](https://charmhub.io/mysql-router) - a machine charm to deploy MySQL Router.
- [tls-certificates-operator](https://charmhub.io/tls-certificates-operator) - TLS operator. **Note**: The TLS settings in bundles use self-signed-certificates which are not recommended for production clusters. The `tls-certificates-operator` charm offers a variety of configurations, read more on the TLS charm [here](https://charmhub.io/tls-certificates-operator).

## Troubleshooting

If you have any problems or questions, please feel free to reach out. We'd be more than glad to help!

The fastest way to get our attention is to create a [discourse post](https://discourse.charmhub.io/).
