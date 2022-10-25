# Canonical Distribution of MySQL + MySQLRouter

Welcome to the Canonical Distribution of MySQL + MySQLRouter.

The objective of this page is to provide directions to get up and running with Canonical MySQL charms.

## Installation

Currently, we support this distribution with Ubuntu 20.04.

To deploy the bundle to a bootstrapped juju controller, simply run

```shell
juju deploy mysql-bundle
```

## Bundle Components
- [mysql](https://charmhub.io/mysql): A k8s charm to deploy MySQL with Group Replication.
- [mysql-router](https://charmhub.io/mysql-router) - a k8s charm to deploy MySQL Router.
- [tls-certificates-operator](https://charmhub.io/tls-certificates-operator) - TLS operator.

## Troubleshooting

If you have any problems or questions, please feel free to reach out. We'd be more than glad to help!

The fastest way to get our attention is to create a [discourse post](https://discourse.charmhub.io/).
