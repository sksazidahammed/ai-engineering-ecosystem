# Coding and Development

**Catalogue version:** 1.5
**Last updated:** 2026-11-12 19:44 IST (UTC+05:30)

| Project | Provisional classification | Source | Status |
|---|---|---|---|
| Superpowers | Multi-agent software-development methodology and composable skills | [Repository](https://github.com/obra/superpowers) | Verified identity; supports multiple coding-agent hosts |
| Matt Pocock Skills | Composable engineering and productivity skills for coding agents | [Repository](https://github.com/mattpocock/skills) | Verified identity; manual vs automatic update paths differ |
| Everything Claude Code (ECC) | Agent-harness configuration, skills, agents, hooks and tooling | [Repository](https://github.com/affaan-m/ECC) | Verified identity; inspect hooks, permissions and official install channels |
| Karpathy-Inspired Skills | Claude Code plugin / agent instruction pack; includes Cursor project rule | [Repository](https://github.com/multica-ai/andrej-karpathy-skills) | Verified identity; provenance note applies |
| Ponytail | Coding-agent skill / workflow focused on concise, maintainable code and stronger review | [Repository](https://github.com/dietrichgebert/ponytail) | Verified identity; benchmark claims are upstream-reported |
| Addy Osmani Agent Skills | Engineering workflow skills and lifecycle commands | [Repository](https://github.com/addyosmani/agent-skills) | Verified identity; portability caveat applies |
| Anthropic Agent Skills | Agent skills collection | [Official repository](https://github.com/anthropics/skills) | Verified identity; details review pending |

## Karpathy-Inspired Skills

- **Repository:** [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)
- **Type:** Claude Code plugin / reusable agent-instruction pack; also includes a Cursor project rule.
- **Purpose:** Reduce common coding-agent failure modes through four principles: think before coding, simplicity first, surgical changes, and goal-driven execution with verifiable success criteria.
- **Installation modes:** Claude Code marketplace plugin or a project-level `CLAUDE.md`; Cursor support is provided through a committed project rule.
- **License:** MIT, as stated in the repository.
- **Provenance caution:** The README's Claude Code marketplace and raw-file installation examples reference `forrestchang/andrej-karpathy-skills`, not the submitted `multica-ai` owner. Confirm the intended canonical source and current plugin instructions before installing.
- **Practical assessment:** A compact, low-friction instruction set for reducing overengineering and unintended edits. It is guidance, not a guarantee of correctness, and it does not replace tests, code review, or explicit project-specific requirements.

## Addy Osmani Agent Skills

- **Repository:** [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)
- **Type:** Multi-agent-compatible engineering skills collection, with nine lifecycle slash commands and agent-specific setup guidance.
- **Workflow:** Define/specify, plan, build, test, constrain, review, web performance audit, simplify, and ship. The README currently describes 25 skills and installation through the `skills` CLI across 70+ agents.
- **Installation:** `npx skills add addyosmani/agent-skills`; list available skills with `--list`. Native setup instructions are provided for several coding agents.
- **Important portability caveat:** The README documents an issue where installing a single skill may omit shared repository-level `references/` files. Follow the upstream workaround or install the full repository when a skill depends on those references.
- **Assessment:** Broad engineering-lifecycle coverage and useful quality gates. Treat `/build auto` as an autonomy feature that still requires review of the plan, permissions and resulting commits.

## Ponytail

- **Repository:** [dietrichgebert/ponytail](https://github.com/dietrichgebert/ponytail)
- **Type:** Coding-agent skill/workflow emphasizing minimal necessary code, reuse of existing project components, validation, and deeper code review/audit.
- **Assessment:** Relevant to reducing overengineering and unnecessary token/code volume without intentionally removing tests, error handling, security or accessibility. Its benchmark figures and comparative claims are reported by the project; they have not been independently reproduced in this directory.

## Additional verified projects

### Superpowers

A complete development methodology built from composable skills and startup instructions. Its workflow emphasizes requirements discovery, design/specification, implementation planning, test-driven development, subagent execution and review. It supports multiple agent hosts; install separately per host. Review requested permissions and hooks before enabling autonomous workflows.

### Matt Pocock Skills

A collection of small, composable skills for practical software engineering and productivity. The README documents setup flows for Claude Code, Codex, Copilot, Gemini CLI and the Agent Skills CLI. The project distinguishes marketplace plugins with automatic updates from copied skill files that require manual updating; avoid installing both variants simultaneously.

### Everything Claude Code (ECC)

An agent-harness configuration system spanning skills, agents, rules, hooks, commands and tooling. The repository lists MIT licensing and publishes multiple install surfaces/packages. Use only official repository, npm and marketplace channels named by upstream. Because hooks and agent tools can execute commands or access project context, inspect them before installation.

## Editorial notes

This category is intended for tools that directly support software development, coding-agent behavior, repository workflows, and engineering practices. Skills are not the same thing as standalone applications or agent frameworks. The classification will be refined after checking each project's current README, supported agents, installation method, license, and maintenance signals.

Do not install a skill into a production coding agent solely on the basis of its name. Review its instructions and scripts first.
