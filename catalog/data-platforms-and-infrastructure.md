# Data Platforms and Infrastructure

**Catalogue version:** 1.12
**Last updated:** 2026-11-12 21:35 IST (UTC+05:30)

| Project | Classification | Official repository | Status |
|---|---|---|---|
| ingestr | CLI and Python library for data ingestion between sources and destinations | [bruin-data/ingestr](https://github.com/bruin-data/ingestr) | FSL-1.1-ALv2; Apache-2.0 future grant after two years |
| HydraDB | Distributed graph database built on S3-compatible object storage | [hydra-db/hydradb](https://github.com/hydra-db/hydradb) | Elastic License 2.0; hosted-service restrictions apply |
| Nhost | Open-source backend platform / Firebase alternative | [nhost/nhost](https://github.com/nhost/nhost) | MIT repository license; hosted and self-hosted operations differ |

## ingestr

- **Project link:** [Official source](https://github.com/bruin-data/ingestr)

- **Type:** Command-line data-ingestion application with a Python SDK.

- **Purpose:** Moves data from supported databases, APIs, files and other sources into supported destinations without requiring users to write a custom pipeline for each connector.

- **Capabilities:** Supports full and incremental loading patterns, including append, merge and delete-plus-insert. The README lists a broad matrix of source and destination connectors; verify the current matrix for the exact systems and direction you need.

- **Installation:** The README documents an install script and `pip install ingestr`. The optional `ingestr[sdk]` package exposes Python ingestion functions and streams rows/DataFrames to the CLI using Arrow IPC by default.

- **License:** Functional Source License 1.1 with an Apache-2.0 future license. The current FSL grant excludes competing commercial products or services; the Apache-2.0 grant becomes effective on the second anniversary of the date the relevant software version was made available. Check the license file for the version you use.

- **Assessment:** Useful for moving data into warehouses and databases with a consistent CLI. Validate connector support, schema behavior, incremental state, credentials and retry semantics before production use. It is a data engineering tool, not an AI agent.

## HydraDB

- **Project link:** [Official source](https://github.com/hydra-db/hydradb)

- **Type:** Distributed graph database written in Rust and designed around S3-compatible object storage.

- **Architecture:** Stores durable graph records, write-ahead logs, manifests and traversal indexes in object storage. Query nodes and indexers can scale independently; local memory and SSD/NVMe state are treated as disposable caches.

- **Query interfaces:** The README documents snapshot-consistent OpenCypher queries, GraphBLAS-backed traversal, Neo4j-compatible Bolt connectivity, and JSON / streaming NDJSON HTTP APIs.

- **Requirements:** Rust 1.91+, a C/C++ toolchain, `libcypher-parser` and SuiteSparse GraphBLAS are listed for building. An S3-compatible object store is required for deployed storage; local development mode is also documented.

- **License:** Elastic License 2.0 (ELv2), not a conventional OSI-approved open-source license. It restricts providing the software to third parties as a hosted or managed service offering substantial functionality. Review the full license before commercial deployment.

- **Assessment:** An infrastructure-oriented option for graph workloads that need durable object-store backing and independently scalable query/indexing tiers. The README includes local smoke tests, but production suitability requires workload benchmarks, failure testing and operational evaluation.

## Nhost

- **Project link:** [Official source](https://github.com/nhost/nhost)

- **Type:** Open-source backend platform and Firebase alternative for application development.

- **Core services:** Combines PostgreSQL, Hasura-powered GraphQL, authentication, file storage, serverless JavaScript/TypeScript functions, and a CLI for local development.

- **AI integration:** The Nhost CLI includes an MCP server for coding assistants. Depending on permissions and environment, it can inspect GraphQL schemas, run allowed queries and mutations, search documentation, and manage local metadata, permissions and migrations.

- **Installation / deployment:** The README documents hosted projects, local development through the Nhost CLI, and self-hosting through Docker Compose. The CLI is distributed through Homebrew, Nix and JavaScript package managers.

- **License / cost:** The repository states MIT licensing for Nhost's open-source code. Hosted platform usage, infrastructure and third-party services may have separate pricing and limits; self-hosting transfers database, storage, compute, backups and maintenance responsibilities to the operator.

- **Security:** GraphQL permissions, authentication configuration, storage access rules, database credentials, secrets and MCP tool permissions must be reviewed carefully. Do not give an agent broad production mutation access by default.

- **Assessment:** Useful for building full-stack applications without assembling every backend service independently. Compare hosted limits and operational costs against self-hosting requirements before choosing it.

## 📝 Note For Reader

Data platforms can move, store or expose large volumes of sensitive information. Test pipelines on non-production data, use least-privilege credentials, verify backup and recovery behavior, and review each project's license before offering it as a hosted service.
