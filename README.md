# Canonical Distribution of MySQL + MySQLRouter

Welcome to the Canonical Distribution of MySQL + MySQLRouter.

The objective of this page is to provide directions to get up and running with Canonical MySQL charms.

## Installation

Currently, we support this distribution with Ubuntu 20.04.

To get started, please install the following:
- LXD
- Juju

Then, please bootstrap the juju controller with microk8s using `juju bootstrap localhost <controller_name>`.

Finally add a juju model with `juju add-model <model-name>` and deploy the bundle with `juju deploy mysql-bundle`.

## Bundle Components
- [mysql](https://charmhub.io/mysql): A k8s charm to deploy MySQL with Group Replication.
- [mysql-router](https://charmhub.io/mysql-router) - a k8s charm to deploy MySQL Router.

## Troubleshooting

If you have any problems or questions, please feel free to reach out. We'd be more than glad to help!

The fastest way to get our attention is to create a [disourse post](https://discourse.charmhub.io/).
