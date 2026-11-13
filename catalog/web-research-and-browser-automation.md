# Web Research and Browser Automation

**Directory version:** 1.16  
**Last updated:** 2026-11-13 18:24 IST (UTC+05:30)

| Project | Classification | Official source | Status |
|---|---|---|---|
| Wigolo | Local-first web intelligence MCP server | [KnockOutEZ/wigolo](https://github.com/KnockOutEZ/wigolo) | AGPL-3.0 stated in README |
| Ego Lite | Browser for AI-agent automation | [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite) | Review browser profile isolation, cookies and authenticated session access before use. |
| Chrome DevTools MCP | Chrome debugging and automation MCP/CLI | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | Upstream explicitly warns that browser content and data are exposed to MCP clients. Do not use with sensitive sessions. |
| Agent Browser | Browser automation CLI for agents | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) | Apache-2.0 stated in README |
| NotebookLM Python | Unofficial NotebookLM/Gemini Notebook API and CLI | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | MIT stated in README |

## Wigolo

- **Project link:** [Official source](https://github.com/KnockOutEZ/wigolo)

- **Type / Classification:** Local-first web intelligence MCP server.

- **Purpose:** Provides web search and retrieval capabilities for AI agents through MCP and REST, with a local-first positioning.

- **Workflow / Requirements:** README describes Node.js 20+, npm distribution and public-beta status.

- **License / Cost / Status:** AGPL-3.0 stated in README; web access can expose queries and retrieved content to the connected agent.

## Ego Lite

- **Project link:** [Official source](https://github.com/citrolabs/ego-lite)

- **Type / Classification:** Browser for AI-agent automation.

- **Purpose:** A browser application designed for agent-driven web automation, with desktop downloads and documentation.

- **Workflow / Requirements:** README lists macOS and Windows installers; Linux support should be checked in current docs.

- **License / Cost / Status:** Review browser profile isolation, cookies and authenticated session access before use.

## Chrome DevTools MCP

- **Project link:** [Official source](https://github.com/ChromeDevTools/chrome-devtools-mcp)

- **Type / Classification:** Chrome debugging and automation MCP/CLI.

- **Purpose:** Exposes live Chrome DevTools capabilities for browser automation, network inspection, screenshots, console review and performance analysis.

- **Workflow / Requirements:** README describes an MCP server and CLI using Puppeteer; officially supports Google Chrome and Chrome for Testing.

- **License / Cost / Status:** Upstream explicitly warns that browser content and data are exposed to MCP clients. Do not use with sensitive sessions.

## Agent Browser

- **Project link:** [Official source](https://github.com/vercel-labs/agent-browser)

- **Type / Classification:** Browser automation CLI for agents.

- **Purpose:** A Rust CLI lets agents navigate pages, read accessibility-tree snapshots and act on page elements through shell commands.

- **Workflow / Requirements:** README documents npm installation and a separate browser installation step.

- **License / Cost / Status:** Apache-2.0 stated in README; browser sessions may expose logged-in data and permit consequential actions.

## NotebookLM Python

- **Project link:** [Official source](https://github.com/teng-lin/notebooklm-py)

- **Type / Classification:** Unofficial NotebookLM/Gemini Notebook API and CLI.

- **Purpose:** Provides programmatic access to notebook features through Python, CLI and agent skills.

- **Workflow / Requirements:** README supports Python 3.10+ and identifies the project as an unofficial library.

- **License / Cost / Status:** MIT stated in README; it relies on undocumented Google APIs that may change and is not affiliated with Google.

## 📝 Note For Reader

Entries are categorized by their primary use. A repository README review verifies the submitted identity and upstream-described scope; it does not constitute hands-on installation, performance, security or legal testing. Recheck current upstream documentation, license files and provider terms before deployment.
