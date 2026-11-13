# Agent Workspaces and Orchestration

**Directory version:** 1.16  
**Last updated:** 2026-11-13 18:24 IST (UTC+05:30)

| Project | Classification | Official source | Status |
|---|---|---|---|
| AG2 | Multi-agent application framework | [ag2ai/ag2](https://github.com/ag2ai/ag2) | Check the framework version and AG2 Classic migration boundary |
| Orca | Parallel coding-agent workspace | [stablyai/orca](https://github.com/stablyai/orca) | MIT stated in README |
| Traycer | AI agent orchestration desktop app | [traycerai/traycer](https://github.com/traycerai/traycer) | Bring-your-own-provider subscriptions/keys may be required |
| Oh My Claude Code | Claude Code multi-agent orchestration layer | [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | MIT stated in README |
| Oh My Codex | Codex CLI orchestration layer | [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | MIT stated in README |
| Paperclip | Agent-team management application | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | Agent management does not remove the need for credential isolation, spending controls and human approval. |
| Multica | Self-hostable agent work-management workspace | [multica-ai/multica](https://github.com/multica-ai/multica) | Source-available wording is used upstream |
| OpenWork | Open-source desktop workspace for agents | [different-ai/openwork](https://github.com/different-ai/openwork) | MIT stated for desktop app |
| cc-haha | Claude Code desktop and mobile workspace | [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha) | Community Source license badge |
| jcode | Parallel coding-agent runtime | [1jehuang/jcode](https://github.com/1jehuang/jcode) | Treat throughput and resource-efficiency claims as upstream claims until independently benchmarked. |
| Background Agents | Background coding-agent orchestration | [ColeMurray/background-agents](https://github.com/ColeMurray/background-agents) | Verification pending |
| LoopX | Agent orchestration candidate | [huangruiteng/loopx](https://github.com/huangruiteng/loopx) | Verification pending |
| Ouroboros (razzant) | Self-evolving general-purpose agent and desktop/CLI runtime | [razzant/ouroboros](https://github.com/razzant/ouroboros) | MIT stated in README; distinct from Q00/ouroboros |


## AG2

- **Project link:** [Official source](https://github.com/ag2ai/ag2)

- **Type / Classification:** Multi-agent application framework.

- **Purpose:** A Python framework for building agentic applications and coordinating agents; current repository distinguishes the protocol-driven framework from AG2 Classic.

- **Workflow / Requirements:** README links documentation, playground, examples and package installation; the legacy AutoGen-style namespace moved to a separate repository.

- **License / Cost / Status:** Check the framework version and AG2 Classic migration boundary; model API use may incur provider charges.

## Orca

- **Project link:** [Official source](https://github.com/stablyai/orca)

- **Type / Classification:** Parallel coding-agent workspace.

- **Purpose:** Runs coding agents such as Claude Code and Codex in parallel, each in its own worktree, with chat/terminal and local/cloud workflows.

- **Workflow / Requirements:** README lists macOS, Windows and Linux desktop releases.

- **License / Cost / Status:** MIT stated in README; review agent permissions and cloud-workspace data handling.

## Traycer

- **Project link:** [Official source](https://github.com/traycerai/traycer)

- **Type / Classification:** AI agent orchestration desktop app.

- **Purpose:** Coordinates multiple agents in parallel, supports agent-to-agent communication and shared context across models/providers.

- **Workflow / Requirements:** README describes a desktop application, downloads, docs and MIT license.

- **License / Cost / Status:** Bring-your-own-provider subscriptions/keys may be required; verify provider terms and local project access.

## Oh My Claude Code

- **Project link:** [Official source](https://github.com/Yeachan-Heo/oh-my-claudecode)

- **Type / Classification:** Claude Code multi-agent orchestration layer.

- **Purpose:** Adds role-based multi-agent workflows and orchestration to Claude Code.

- **Workflow / Requirements:** README documents npm installation, workflow documentation and a separate Codex counterpart.

- **License / Cost / Status:** MIT stated in README; inspect hooks, subagents and shell permissions before enabling.

## Oh My Codex

- **Project link:** [Official source](https://github.com/Yeachan-Heo/oh-my-codex)

- **Type / Classification:** Codex CLI orchestration layer.

- **Purpose:** Adds prompts, workflows and runtime assistance to OpenAI Codex CLI.

- **Workflow / Requirements:** README documents npm installation and integrations with other agent runtimes.

- **License / Cost / Status:** MIT stated in README; review configured tools and permissions.

## Paperclip

- **Project link:** [Official source](https://github.com/paperclipai/paperclip)

- **Type / Classification:** Agent-team management application.

- **Purpose:** A management application for organizing AI agents as a coordinated team with work assignments and oversight.

- **Workflow / Requirements:** README links quickstart, documentation and a self-hostable application; MIT license badge is present.

- **License / Cost / Status:** Agent management does not remove the need for credential isolation, spending controls and human approval.

## Multica

- **Project link:** [Official source](https://github.com/multica-ai/multica)

- **Type / Classification:** Self-hostable agent work-management workspace.

- **Purpose:** Assigns work to AI coding agents through a shared board; agents report progress, blockers and handoffs for review.

- **Workflow / Requirements:** README describes compatibility with existing agent CLIs and self-hosting.

- **License / Cost / Status:** Source-available wording is used upstream; inspect exact license before commercial use.

## OpenWork

- **Project link:** [Official source](https://github.com/different-ai/openwork)

- **Type / Classification:** Open-source desktop workspace for agents.

- **Purpose:** A desktop workspace for agents operating on local files, with multiple model providers, shared skills and MCP servers.

- **Workflow / Requirements:** README describes macOS, Windows and Linux support, local models through Ollama and optional team/admin workflows.

- **License / Cost / Status:** MIT stated for desktop app; connected agents can access local files and integrations.

## cc-haha

- **Project link:** [Official source](https://github.com/NanmiCoder/cc-haha)

- **Type / Classification:** Claude Code desktop and mobile workspace.

- **Purpose:** A desktop workbench for Claude Code sessions, permissions, worktrees, browser preview, MCP/subagent management and remote mobile control.

- **Workflow / Requirements:** README describes desktop clients and companion mobile/H5 access; platform-specific computer-use behavior differs.

- **License / Cost / Status:** Community Source license badge; inspect LICENSE before reuse. Remote access and computer-use permissions are sensitive.

## jcode

- **Project link:** [Official source](https://github.com/1jehuang/jcode)

- **Type / Classification:** Parallel coding-agent runtime.

- **Purpose:** Aims to run many coding agents concurrently with lower memory overhead and reduced machine contention.

- **Workflow / Requirements:** README links releases and describes a high-performance agent workflow; exact runtime requirements should be checked upstream.

- **License / Cost / Status:** Treat throughput and resource-efficiency claims as upstream claims until independently benchmarked.

## Background Agents

- **Project link:** [Official source](https://github.com/ColeMurray/background-agents)

- **Type / Classification:** Background coding-agent orchestration.

- **Purpose:** Repository identity was not confirmed through the available README fetch; retained as a discovery candidate based on the submitted canonical URL.

- **Workflow / Requirements:** README fetch was unavailable in this intake; do not infer implementation details from the name.

- **License / Cost / Status:** Verification pending; confirm repository existence, purpose and license before relying on it.

## LoopX

- **Project link:** [Official source](https://github.com/huangruiteng/loopx)

- **Type / Classification:** Agent orchestration candidate.

- **Purpose:** Repository identity was not confirmed through the available README fetch; retained as an unresolved candidate.

- **Workflow / Requirements:** README fetch was unavailable in this intake; project function is not asserted.

- **License / Cost / Status:** Verification pending; distinguish from other projects with similar names.

## Ouroboros (razzant)

- **Project link:** [Official source](https://github.com/razzant/ouroboros)

- **Type / Classification:** General-purpose self-evolving AI agent with desktop and headless CLI interfaces.

- **Purpose:** Upstream describes an agent with persistent identity, durable memory and task history that can coordinate specialist agents and modify its own implementation.

- **Workflow / Requirements:** README lists Python 3.10+, macOS 12+ and Linux/Windows support, with local state and remote model inference options.

- **License / Caveat:** MIT badge is present in the README. Self-modifying agent behavior and remote inference require careful permission, data-flow and rollback controls.

- **Assessment:** A distinct agent-runtime project; it must not be merged with `Q00/ouroboros`, which is a separate spec-first coding workflow.

## 📝 Note For Reader

Entries are categorized by their primary use. A repository README review verifies the submitted identity and upstream-described scope; it does not constitute hands-on installation, performance, security or legal testing. Recheck current upstream documentation, license files and provider terms before deployment.
