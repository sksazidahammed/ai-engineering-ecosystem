# Productivity and Workflows

**Catalogue version:** 1.14
**Last updated:** 2026-11-13 00:55 IST (UTC+05:30)

| Project | Classification | Official repository | Status |
|---|---|---|---|
| OpenReply | Self-hosted Instagram comment-to-DM automation | [diwenne/openreply](https://github.com/diwenne/openreply) | Repository identity verified; Meta API and hosting requirements apply |
| OpnForm | Open-source form builder with MCP integration | [opnform/opnform](https://github.com/opnform/opnform) | Repository identity verified; AGPL-3.0 stated upstream |
| OpenLore | Agent-native shared knowledge repository with SSH, MCP and governed file access | [aakarim/OpenLore](https://github.com/aakarim/OpenLore) | Apache-2.0; access policy and deployment configuration require care |

## OpenReply

- **Project link:** [Official source](https://github.com/diwenne/openreply)

- **Type:** Self-hosted Instagram comment-to-DM automation application.

- **Function:** Keyword-triggered private replies, optional public replies, tracked links, campaign management, inbox and logs, using Meta's official Instagram API.

- **Infrastructure:** Requires a deployed web app, PostgreSQL, Redis, a background worker, public HTTPS and email delivery. The README clarifies that its public demo is not a hosted service.

- **License:** MIT, according to upstream. The optional Zernio connection provider is paid; hosting costs are separate.

- **Caveat:** Instagram account type, Meta permissions, messaging windows, rate limits and platform policies apply.

## OpnForm

- **Project link:** [Official source](https://github.com/opnform/opnform)

- **Type:** Open-source no-code form builder, with hosted and self-hosted deployment options.

- **Features:** Form fields, embeds, notifications, integrations, logic, CAPTCHA and analytics. Its README also documents an MCP server for AI-assisted form drafting and workspace operations.

- **License:** AGPL-3.0, as indicated by the upstream README. Review the license obligations before modifying or offering a hosted derivative.

## OpenLore

- **Project link:** [Official source](https://github.com/aakarim/OpenLore)

- **Type:** Agent-native knowledge repository and self-hostable server that exposes shared files through SSH, SFTP/SSHFS, MCP and a web interface.

- **Purpose:** Gives multiple agents, repositories and people a common, inspectable knowledge surface using ordinary Markdown and files rather than a separate vector database or ingestion pipeline.

- **Workflow / architecture:** Mounts document sets into an identity-scoped virtual filesystem. Read-only access is the default; configured identities can receive scoped publishing or write permissions. Writes are validated and committed atomically with conflict checks.

- **Installation:** The README documents Homebrew installation and Linux/Windows quick-start paths. A local server exposes SSH on port 2222 and web/MCP on port 8080 by default; hosted deployment requires persistent storage and deployment-specific network configuration.

- **Integrations:** The README documents Claude Code, Codex, Cursor, OpenCode, CI jobs and other shell-capable agents through MCP or SSH.

- **License:** Apache-2.0. Third-party components retain their own notices and licenses.

- **Security:** The normal shell is a constrained in-memory Go interpreter rather than an operating-system shell. Nevertheless, identity grants, public endpoints, SSH/OAuth configuration, write permissions, persistent storage and deployment secrets need careful configuration. Keep sensitive docsets private and grant least privilege.

- **Assessment:** Useful when several agents or people need shared, governed project knowledge. For one agent in one repository, ordinary version-controlled Markdown may be simpler.

## Onyx

- **Project link:** [Official source](https://github.com/onyx-dot-app/onyx)

- **Type:** Self-hostable team knowledge platform and AI context layer, with web application, connectors, agent runtime and MCP server.

- **Purpose:** Connects organizational knowledge across 50+ applications, indexes content with metadata and permissions, and makes it searchable for chat, retrieval-augmented generation (RAG), deep research and AI agents.

- **Workflow / architecture:** Syncs content from connected sources into an internal representation, then retrieves relevant documents for user queries and agent tasks. Supports hybrid keyword/vector retrieval, web search, external actions, code sandboxes, artifacts and voice. Agents can use connected knowledge while respecting the configured user permissions.

- **Installation / deployment:** The README documents a one-command installer and Docker, Kubernetes, Helm and Terraform deployment paths. Standard deployment includes indexing, background workers, Redis and MinIO components; Onyx Lite is a smaller chat/agent stack (README states under 1 GB memory) but cannot index documents.

- **Integrations:** 50+ knowledge connectors, major hosted and self-hosted LLM providers, web-search services, Slack, Discord, Chrome extension, embeddable widget and MCP clients such as Claude Code, OpenCode and Codex.

- **License / cost:** Community Edition core is MIT. Enterprise-only code under `ee` directories is governed by the separate Onyx Enterprise License. Onyx Cloud and enterprise capabilities have separate commercial terms; check current pricing and feature boundaries before deployment.

- **Privacy / security:** Self-hosted and air-gapped deployment options keep document indexes and processing within the operator's environment. However, connected source credentials, document permissions, embeddings, model-provider routing, web search, external actions and sandbox execution all need careful configuration. Self-hosting alone does not guarantee that prompts or indexed data never leave the environment.

- **Limitations:** Full indexing requires the Standard stack and more infrastructure than Lite. Connector coverage, sync reliability, model quality and resource requirements depend on the selected deployment and integrations. Review current documentation for connector-specific permissions and operational prerequisites.

- **Assessment:** A substantial team knowledge and agent platform, especially relevant when a company needs governed access to internal information across multiple systems. It is considerably heavier than a personal chat interface.

## 📝 Note For Reader

This category is reserved for AI tools/ that support personal or team workflows, task management, document operations, knowledge organization, and cross-application automation, where those tools do not fit more specific catalogues. Workflow automation can move or modify data across connected services. Before enabling it, inspect the scopes requested, confirm where data is stored, and test with non-sensitive data.
