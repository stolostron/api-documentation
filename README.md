# Advanced Cluster Management (ACM) API Documentation

Welcome to the API documentation repository for **Red Hat Advanced Cluster Management for Kubernetes (ACM)**. This repository provides detailed documentation for the core and extended APIs that power ACM and its ecosystem.

## Overview

Advanced Cluster Management (ACM) enables you to manage multiple Kubernetes clusters, including OpenShift and other Kubernetes distributions, from a single control plane. ACM provides capabilities for cluster lifecycle management, application lifecycle, governance, risk, compliance, storage, container native virtualization, networking and edge management as well as observability across clusters.

This repository contains:
- **Custom Resource Definition (CRDs) API documentation** for ACM core components
- Links to API documentation for ACM add-ons and related open source projects

## Core API Documentation

The core API documentation, including all ACM CRDs and their detailed specifications, can be found in the [api-docs/README.md](./api-docs/README.md).
<br>
* [Release-2.14](https://github.com/stolostron/api-documentation/blob/release-2.14/api-docs/README.md)
* [PRE-Release-2.15](https://github.com/stolostron/api-documentation/blob/release-2.15/api-docs/README.md)

## External ACM-Related API Documentation

ACM integrates with and extends many open source projects. Below are links to API documentation for key external components and add-ons commonly used with ACM:

- **[Gatekeeper (OPA)](https://open-policy-agent.github.io/gatekeeper/website/docs/)
  - Policy and governance for Kubernetes clusters.
- **[VolSync](https://backube.github.io/volsync/)
  - Asynchronous data replication for Kubernetes volumes, used for backup and disaster recovery in ACM-managed clusters.
- **[Submariner](https://submariner.io/docs/)
  - Enables direct networking between pods and services in different Kubernetes clusters.
- **[Open Cluster Management (OCM) APIs](https://open-cluster-management.io/docs/concepts/architecture/)
  - The upstream open source project powering ACM.
- **[Cluster Lifecycle API (stolostron/cluster-lifecycle-api)](https://github.com/stolostron/cluster-lifecycle-api)
  - Types and concepts for cluster lifecycle management in ACM and MCE.
- **[Kubernetes Gateway API](https://gateway-api.sigs.k8s.io/)
  - Next-generation service networking APIs, often used with ACM for advanced traffic management.

> _If you have additional ACM-related API documentation to link here, please submit a pull request!_

## Generating API Documentation

To generate API documentation for the core ACM product (including multiclusterhub-operator, backplane-operator, and OCM):

```sh
make generate
```

You will be prompted for the release and backplane version numbers. The `release-` and `backplane-` prefixes are filled in automatically.

This command will:
1. Clone the required repositories (multiclusterhub-operator, backplane-operator, ocm)
2. Extract CRDs from the cloned repositories
3. Generate API documentation from the CRDs
4. Clean up the cloned repositories

Run `make help` to see all available commands.

## Contributing

Contributions to this documentation are welcome! Please open issues or pull requests for corrections, improvements, or to add links to additional ACM-related API documentation.

## License

This repository is licensed under the [Apache 2.0 License](./LICENSE).

## Setting Up a New Release

To add a workflow for a new release:

```sh
make init-release
```

You will be prompted for the release version (e.g. `2.16`) and backplane version (e.g. `2.11`), then asked to confirm. This generates a new workflow file (e.g. `.github/workflows/generate-api-docs-release-2.16.yml`) on `main`.

The `release-X.Y` branch must exist in the remote before the workflow can run. The scheduled cron job runs the workflow from `main`, checks out the release branch, generates docs, and commits them back to the release branch.
