# Coding Agent CLIs and Harnesses

**Catalogue version:** 1.16  
**Last updated:** 2026-11-13 18:24 IST (UTC+05:30)

| Project | Classification | Official source | Status |
|---|---|---|---|
| OpenAI Codex | Local coding-agent CLI | [openai/codex](https://github.com/openai/codex) | Provider authentication and model usage are subject to OpenAI account and product terms |
| OpenCode | Open-source AI coding agent | [anomalyco/opencode](https://github.com/anomalyco/opencode) | Review provider configuration, shell/file permissions and current license before deployment. |
| Forge | AI-enhanced terminal development environment | [tailcallhq/forgecode](https://github.com/tailcallhq/forgecode) | Review command execution permissions and configured model-provider data handling. |
| Kimi CLI (archived) | Archived Python coding-agent CLI | [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | Archived |
| Open Interpreter | Local coding and computer-use agent | [openinterpreter/openinterpreter](https://github.com/openinterpreter/openinterpreter) | Code execution and computer interaction can affect local files and systems. Use least privilege and review commands. |
| Pi | Minimal extensible coding-agent harness | [earendil-works/pi](https://github.com/earendil-works/pi) | Review third-party extensions and tool permissions |
| Oh My Pi | IDE-integrated coding agent | [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | Inspect its license and dependency/runtime requirements before installing |

## OpenAI Codex

- **Project link:** [Official source](https://github.com/openai/codex)

- **Type / Classification:** Local coding-agent CLI.

- **Purpose:** Runs an AI coding agent locally and can work through terminal, IDE integrations and a desktop app.

- **Workflow / Requirements:** README documents Windows, macOS and Linux installation paths, npm and Homebrew distribution.

- **License / Cost / Status:** Provider authentication and model usage are subject to OpenAI account and product terms; agent execution can access local files and commands.

## OpenCode

- **Project link:** [Official source](https://github.com/anomalyco/opencode)

- **Type / Classification:** Open-source AI coding agent.

- **Purpose:** A terminal-based coding agent with a provider-flexible workflow and a broader extension ecosystem.

- **Workflow / Requirements:** README links to the official website, npm CLI package and release workflow.

- **License / Cost / Status:** Review provider configuration, shell/file permissions and current license before deployment.

## Forge

- **Project link:** [Official source](https://github.com/tailcallhq/forgecode)

- **Type / Classification:** AI-enhanced terminal development environment.

- **Purpose:** Combines an interactive terminal UI, one-shot CLI mode and a Zsh workflow for AI-assisted development.

- **Workflow / Requirements:** README documents a shell installer and agent, workspace and shell integrations.

- **License / Cost / Status:** Review command execution permissions and configured model-provider data handling.

## Kimi CLI (archived)

- **Project link:** [Official source](https://github.com/MoonshotAI/kimi-cli)

- **Type / Classification:** Archived Python coding-agent CLI.

- **Purpose:** Historical terminal agent from Moonshot AI; the upstream repository explicitly says it is archived and superseded by Kimi Code CLI.

- **Workflow / Requirements:** The repository is read-only and upstream provides migration instructions to `MoonshotAI/kimi-code`.

- **License / Cost / Status:** Archived; no further releases, fixes or security updates. Use the successor for current deployments.

## Open Interpreter

- **Project link:** [Official source](https://github.com/openinterpreter/openinterpreter)

- **Type / Classification:** Local coding and computer-use agent.

- **Purpose:** A coding agent designed to operate through a terminal and execute tasks using configured models and tools.

- **Workflow / Requirements:** README documents platform installers and an Apache-2.0 license badge; current installation details are upstream.

- **License / Cost / Status:** Code execution and computer interaction can affect local files and systems. Use least privilege and review commands.

## Pi

- **Project link:** [Official source](https://github.com/earendil-works/pi)

- **Type / Classification:** Minimal extensible coding-agent harness.

- **Purpose:** A customizable agent harness with extensions, skills, prompt templates, themes and packages.

- **Workflow / Requirements:** README documents CLI, JSON/print mode, RPC and a TypeScript SDK.

- **License / Cost / Status:** Review third-party extensions and tool permissions; repository guidance says new contributor issues/PRs may be auto-closed by default.

## Oh My Pi

- **Project link:** [Official source](https://github.com/can1357/oh-my-pi)

- **Type / Classification:** IDE-integrated coding agent.

- **Purpose:** A coding agent with an integrated IDE-style workflow, built from the Pi ecosystem.

- **Workflow / Requirements:** README identifies npm distribution, TypeScript/Rust components and Bun runtime.

- **License / Cost / Status:** Inspect its license and dependency/runtime requirements before installing; capabilities are upstream-described.

## 📝 Note For Reader

Entries are categorized by their primary use. A repository README review verifies the submitted identity and upstream-described scope; it does not constitute hands-on installation, performance, security or legal testing. Recheck current upstream documentation, license files and provider terms before deployment.
