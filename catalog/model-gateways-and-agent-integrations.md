# Model Gateways and Agent Integrations

**Directory version:** 1.16  
**Last updated:** 2026-11-13 18:24 IST (UTC+05:30)

| Project | Classification | Official source | Status |
|---|---|---|---|
| Claude Code Router | Local model gateway and control plane | [musistudio/claude-code-router](https://github.com/musistudio/claude-code-router) | Inspect provider routing, credential storage and request logs |
| OpenAI OAuth | OAuth integration and OpenAI-compatible proxy | [EvanZhouDev/openai-oauth](https://github.com/EvanZhouDev/openai-oauth) | Review account terms and credential handling carefully. Do not assume this is an official OpenAI SDK or an endorsed API entitlement. |
| Corsair | Application integration and OAuth connection platform | [corsairdev/corsair](https://github.com/corsairdev/corsair) | Review connector scopes, token storage, webhook verification and hosted-service terms. |
| Desktop Commander MCP | Desktop filesystem and terminal MCP server | [wonderwhy-er/DesktopCommanderMCP](https://github.com/wonderwhy-er/DesktopCommanderMCP) | High privilege: restrict filesystem roots and shell access, review commands and avoid exposing sensitive files or long-lived credentials. |
| Agent Toolkit for AWS | Official AWS coding-agent toolkit | [aws/agent-toolkit-for-aws](https://github.com/aws/agent-toolkit-for-aws) | Apache-2.0 stated in README |

## Claude Code Router

- **Project link:** [Official source](https://github.com/musistudio/claude-code-router)

- **Type / Classification:** Local model gateway and control plane.

- **Purpose:** Routes coding-agent and compatible API requests across configured providers, with failover, extensions and request observability.

- **Workflow / Requirements:** README describes a desktop application and local gateway workflow.

- **License / Cost / Status:** Inspect provider routing, credential storage and request logs; model subscriptions and API usage remain subject to provider terms.

## OpenAI OAuth

- **Project link:** [Official source](https://github.com/EvanZhouDev/openai-oauth)

- **Type / Classification:** OAuth integration and OpenAI-compatible proxy.

- **Purpose:** Provides sign-in and client adapters intended to let applications connect through a user's ChatGPT account, alongside a local proxy workflow.

- **Workflow / Requirements:** README documents a CLI/dev proxy, React component and OpenAI-compatible clients.

- **License / Cost / Status:** Review account terms and credential handling carefully. Do not assume this is an official OpenAI SDK or an endorsed API entitlement.

## Corsair

- **Project link:** [Official source](https://github.com/corsairdev/corsair)

- **Type / Classification:** Application integration and OAuth connection platform.

- **Purpose:** Provides a REST-based integration layer for connecting users' third-party apps to agents, backend services and customer dashboards.

- **Workflow / Requirements:** README describes a self-hostable core and an optional hosted Hub for OAuth refresh and webhooks.

- **License / Cost / Status:** Review connector scopes, token storage, webhook verification and hosted-service terms.

## Desktop Commander MCP

- **Project link:** [Official source](https://github.com/wonderwhy-er/DesktopCommanderMCP)

- **Type / Classification:** Desktop filesystem and terminal MCP server.

- **Purpose:** Lets agents search, update and manage files, run terminal commands and work with local processes through MCP.

- **Workflow / Requirements:** README documents npm installation and file/terminal workflows.

- **License / Cost / Status:** High privilege: restrict filesystem roots and shell access, review commands and avoid exposing sensitive files or long-lived credentials.

## Agent Toolkit for AWS

- **Project link:** [Official source](https://github.com/aws/agent-toolkit-for-aws)

- **Type / Classification:** Official AWS coding-agent toolkit.

- **Purpose:** Provides coding agents with AWS service knowledge, tools and guardrails for building, deploying and managing applications on AWS.

- **Workflow / Requirements:** README documents AWS CLI configuration and plugins for Claude Code, including AWS core and agent workflows.

- **License / Cost / Status:** Apache-2.0 stated in README; cloud credentials and deployment permissions must follow least privilege.

## 📝 Note For Reader

Entries are categorized by their primary use. A repository README review verifies the submitted identity and upstream-described scope; it does not constitute hands-on installation, performance, security or legal testing. Recheck current upstream documentation, license files and provider terms before deployment.
