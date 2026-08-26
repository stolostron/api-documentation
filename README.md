# Advanced Cluster Management API Documentation

Welcome to the API documentation repository for **Red Hat Advanced Cluster Management for Kubernetes**. This repository provides detailed documentation for the core and extended APIs that power Red Hat Advanced Cluster Management for Kubernetes and the ecosystem.

## Overview

Red Hat Advanced Cluster Management for Kubernetes enables you to manage multiple Kubernetes clusters, including OpenShift and other Kubernetes distributions, from a single control plane. Red Hat Advanced Cluster Management provides capabilities for cluster lifecycle management, application lifecycle, governance, risk, compliance, storage, container native virtualization, networking and edge management as well as observability across clusters.

This repository contains:
- **Custom Resource Definition (CRDs) API documentation** for core components
- Links to API documentation for add-ons and related open source projects

## Core API Documentation

The core Red Hat Advanced Cluster Management for Kubernetes API documentation, including all CRDs and the detailed specifications, is in the [api-docs/README.md](./api-docs/README.md).
<br>
* [Release-2.14](https://github.com/stolostron/api-documentation/blob/release-2.14/api-docs/README.md)
* [Release-2.15](https://github.com/stolostron/api-documentation/blob/release-2.15/api-docs/README.md)
* [Release-2.16](https://github.com/stolostron/api-documentation/blob/release-2.16/api-docs/README.md)
* [Release-2.17](https://github.com/stolostron/api-documentation/blob/release-2.17/api-docs/README.md)

## External Red Hat Advanced Cluster Management-Related API Documentation

Red Hat Advanced Cluster Management integrates with and extends many open source projects. See the following links to API documentation for key external components and add-ons commonly used with the product:

- **[Gatekeeper (OPA)](https://open-policy-agent.github.io/gatekeeper/website/docs/)
  - Policy and governance for Kubernetes clusters.
- **[VolSync](https://backube.github.io/volsync/)
  - Asynchronous data replication for Kubernetes volumes, used for backup and disaster recovery in Red Hat Advanced Cluster Management-managed clusters.
- **[Submariner](https://submariner.io/docs/)
  - Enables direct networking between pods and services in different Kubernetes clusters.
- **[Open Cluster Management (OCM) APIs](https://open-cluster-management.io/docs/concepts/architecture/)
  - The upstream open source project powering ACM.
- **[Cluster Lifecycle API (stolostron/cluster-lifecycle-api)](https://github.com/stolostron/cluster-lifecycle-api)
  - Types and concepts for cluster lifecycle management in Red Hat Advanced Cluster Management and Multicluster Engine.
- **[Kubernetes Gateway API](https://gateway-api.sigs.k8s.io/)
  - Next-generation service networking APIs, often used with the product for advanced traffic management.

> _If you have additional API documentation to link here, submit a pull request._

## Generating API Documentation

To generate API documentation for the core product, including the `multiclusterhub-operator`, `backplane-operator`, and `OCM`, see the following process:

Run the following command:

```sh
make generate
```

You are prompted for the release and backplane version numbers. The `release-` and `backplane-` prefixes are filled in automatically.

The command completes the following tasks:

1. Clones the required repositories (`multiclusterhub-operator`, `backplane-operator`, and `OCM`)
2. Extracts CRDs from the cloned repositories
3. Generates API documentation from the CRDs
4. Cleans up the cloned repositories

Run `make help` to see all available commands.

## Contributing

Contributions to this documentation are welcome. Open issues or pull requests for corrections, improvements, or to add links to additional Red Hat Advanced Cluster Management-related API documentation.

**Important:** All pull requests that change the `Overview` or `Description` of the CRDs require a peer review from the documentation team in the pull request.

## License

This repository is licensed by the [Apache 2.0 License](./LICENSE).

## Setting Up a New Release

To add a workflow for a new release:

```sh
make init-release
```

You are prompted for the release version, for example `2.16`, and the backplane version, for example `2.11`. Then you are prompted to confirm. This generates a new workflow file, for example `.github/workflows/generate-api-docs-release-2.16.yml` on the  `main` branch.

The `release-X.Y` branch must exist in the remote before the workflow can run. The scheduled cron job runs the workflow from `main`, checks out the release branch, generates docs, and commits them back to the release branch.
