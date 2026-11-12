# Coding and Development

****Catalogue version:** 1.10**  
**Last updated:** 2026-11-12 20:54 IST (UTC+05:30)

| Project | Provisional classification | Source | Status |
|---|---|---|---|
| Superpowers | Multi-agent software-development methodology and composable skills | [Repository](https://github.com/obra/superpowers) | Verified identity; supports multiple coding-agent hosts |
| Matt Pocock Skills | Composable engineering and productivity skills for coding agents | [Repository](https://github.com/mattpocock/skills) | Verified identity; manual vs automatic update paths differ |
| Everything Claude Code (ECC) | Agent-harness configuration, skills, agents, hooks and tooling | [Repository](https://github.com/affaan-m/ECC) | Verified identity; inspect hooks, permissions and official install channels |
| Karpathy-Inspired Skills | Claude Code plugin / agent instruction pack; includes Cursor project rule | [Repository](https://github.com/multica-ai/andrej-karpathy-skills) | Verified identity; provenance note applies |
| Ponytail | Coding-agent skill / workflow focused on concise, maintainable code and stronger review | [Repository](https://github.com/dietrichgebert/ponytail) | Verified identity; benchmark claims are upstream-reported |
| Addy Osmani Agent Skills | Engineering workflow skills and lifecycle commands | [Repository](https://github.com/addyosmani/agent-skills) | Verified identity; portability caveat applies |
| Anthropic Agent Skills | Agent skills collection | [Official repository](https://github.com/anthropics/skills) | Verified identity; details review pending |

## Superpowers

- **Project link:** [Official source](https://github.com/obra/superpowers)

- **Type:** Composable software-development methodology and agent-skill collection.

- **Purpose:** Guides coding agents through requirements discovery, design/specification, implementation planning, test-driven development, subagent execution and review.

- **Compatibility:** Supports multiple agent hosts; install and configure it separately for each host.

- **Security:** Review requested permissions, hooks and tool access before enabling autonomous workflows.

- **Assessment:** Useful as an end-to-end development process, but it does not replace human review or project-specific engineering standards.

## Matt Pocock Skills

- **Project link:** [Official source](https://github.com/mattpocock/skills)

- **Type:** Collection of small, composable skills for software engineering and developer productivity.

- **Compatibility:** The README documents setup flows for Claude Code, Codex, Copilot, Gemini CLI and the Agent Skills CLI.

- **Update behavior:** Marketplace plugins support automatic updates; copied skill files require manual updating.

- **Installation caution:** Avoid installing both variants simultaneously, as this can create duplicate or conflicting skill definitions.

- **Assessment:** Useful when selecting individual, focused engineering workflows rather than adopting a single large agent framework.

## Everything Claude Code (ECC)

- **Project link:** [Official source](https://github.com/affaan-m/ECC)

- **Type:** Agent-harness configuration system spanning skills, agents, rules, hooks, commands and supporting tools.

- **Capabilities:** Provides reusable agent behavior and workflow configuration across multiple install surfaces/packages.

- **License:** MIT, according to the repository.

- **Installation:** Use only the official repository, npm packages and marketplace channels named by upstream.

- **Security:** Hooks and agent tools may execute commands or access project context. Inspect scripts, permissions and requested capabilities before installation.

- **Assessment:** A broad configuration ecosystem for tailoring coding agents; review individual components rather than treating the entire bundle as risk-free.

## Karpathy-Inspired Skills

- **Project link:** [Official source](https://github.com/multica-ai/andrej-karpathy-skills)

- **Type:** Claude Code plugin / reusable agent-instruction pack; also includes a Cursor project rule.

- **Purpose:** Reduce common coding-agent failure modes through four principles: think before coding, simplicity first, surgical changes, and goal-driven execution with verifiable success criteria.

- **Installation modes:** Claude Code marketplace plugin or a project-level `CLAUDE.md`; Cursor support is provided through a committed project rule.

- **License:** MIT, as stated in the repository.

- **Provenance caution:** The README's Claude Code marketplace and raw-file installation examples reference `forrestchang/andrej-karpathy-skills`, not the submitted `multica-ai` owner. Confirm the intended canonical source and current plugin instructions before installing.

- **Practical assessment:** A compact, low-friction instruction set for reducing overengineering and unintended edits. It is guidance, not a guarantee of correctness, and it does not replace tests, code review, or explicit project-specific requirements.

## Ponytail

- **Project link:** [Official source](https://github.com/dietrichgebert/ponytail)

- **Type:** Coding-agent skill/workflow emphasizing minimal necessary code, reuse of existing project components, validation, and deeper code review/audit.

- **Assessment:** Relevant to reducing overengineering and unnecessary token/code volume without intentionally removing tests, error handling, security or accessibility. Its benchmark figures and comparative claims are reported by the project; they have not been independently reproduced in this directory.

## Addy Osmani Agent Skills

- **Project link:** [Official source](https://github.com/addyosmani/agent-skills)

- **Type:** Multi-agent-compatible engineering skills collection, with nine lifecycle slash commands and agent-specific setup guidance.

- **Workflow:** Define/specify, plan, build, test, constrain, review, web performance audit, simplify, and ship. The README currently describes 25 skills and installation through the `skills` CLI across 70+ agents.

- **Installation:** `npx skills add addyosmani/agent-skills`; list available skills with `--list`. Native setup instructions are provided for several coding agents.

- **Important portability caveat:** The README documents an issue where installing a single skill may omit shared repository-level `references/` files. Follow the upstream workaround or install the full repository when a skill depends on those references.

- **Assessment:** Broad engineering-lifecycle coverage and useful quality gates. Treat `/build auto` as an autonomy feature that still requires review of the plan, permissions and resulting commits.

## Anthropic Agent Skills

- **Project link:** [Official source](https://github.com/anthropics/skills)

- **Type:** Open collection of reusable agent skills.

- **Purpose:** Provides task-specific instruction packages that extend compatible AI agents with repeatable workflows and domain guidance. The repository is a collection of skills rather than a single standalone application.

- **Use:** Review each skill's own instructions, required tools, scripts and dependencies before installing it into a coding agent. Compatibility and behavior depend on the host agent and the individual skill.

- **License and limitations:** Check the repository's current license and any skill-specific notices before reuse. A skill's presence in the collection does not establish that it is safe, maintained or suitable for every project.

## 📝 Note For Reader

Check the official project source for current requirements, permissions, pricing and license terms before installation or use.
