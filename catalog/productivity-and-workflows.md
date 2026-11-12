# Productivity and Workflows

**Catalogue version:** 1.13
**Last updated:** 2026-11-12 21:55 IST (UTC+05:30)

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

## 📝 Note For Reader

This category is reserved for AI tools/ that support personal or team workflows, task management, document operations, knowledge organization, and cross-application automation, where those tools do not fit more specific catalogues. Workflow automation can move or modify data across connected services. Before enabling it, inspect the scopes requested, confirm where data is stored, and test with non-sensitive data.
