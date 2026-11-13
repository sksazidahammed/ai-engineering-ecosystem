# Coding and Development

**Catalogue version:** 1.16
**Last updated:** 2026-11-13 18:24 IST (UTC+05:30)

| Project | Provisional classification | Source | Status |
|---|---|---|---|
| Superpowers | Multi-agent software-development methodology and composable skills | [Repository](https://github.com/obra/superpowers) | Verified identity; supports multiple coding-agent hosts |
| Matt Pocock Skills | Composable engineering and productivity skills for coding agents | [Repository](https://github.com/mattpocock/skills) | Verified identity; manual vs automatic update paths differ |
| Everything Claude Code (ECC) | Agent-harness configuration, skills, agents, hooks and tooling | [Repository](https://github.com/affaan-m/ECC) | Verified identity; inspect hooks, permissions and official install channels |
| Karpathy-Inspired Skills | Claude Code plugin / agent instruction pack; includes Cursor project rule | [Repository](https://github.com/multica-ai/andrej-karpathy-skills) | Verified identity; provenance note applies |
| Ponytail | Coding-agent skill / workflow focused on concise, maintainable code and stronger review | [Repository](https://github.com/dietrichgebert/ponytail) | Verified identity; benchmark claims are upstream-reported |
| Addy Osmani Agent Skills | Engineering workflow skills and lifecycle commands | [Repository](https://github.com/addyosmani/agent-skills) | Verified identity; portability caveat applies |
| Anthropic Agent Skills | Agent skills collection | [Official repository](https://github.com/anthropics/skills) | Verified identity; details review pending |
| Gentle-AI | Deterministic engineering environment, skills and workflows for coding agents | [Gentleman-Programming/gentle-ai](https://github.com/Gentleman-Programming/gentle-ai) | README and MIT badge reviewed; agent permissions require review |
| Google Agent Skills | Vendor-authored Agent Skills collection for Google products and technologies | [google/skills](https://github.com/google/skills) | Repository identity verified; skill-by-skill requirements vary |
| Agent Skills Specification | Open format/specification for portable agent skills | [agentskills/agentskills](https://github.com/agentskills/agentskills) | Specification repository; not an installable skill pack |
| Vercel Skills CLI | CLI for discovering and installing skills from the open agent-skills ecosystem | [vercel-labs/skills](https://github.com/vercel-labs/skills) | MIT stated upstream |
| Cursor Plugins | Official Cursor plugin collection | [cursor/plugins](https://github.com/cursor/plugins) | Repository identity verified; plugin-specific terms may vary |
| Jakub Krehel Skills | Agent skills for interface design and design engineering | [jakubkrehel/skills](https://github.com/jakubkrehel/skills) | Repository identity verified; license not confirmed in this intake |
| Unslop | Design-oriented agent skill for improving AI-generated interfaces | [heydamir/unslop](https://github.com/heydamir/unslop) | Repository identity verified; license not confirmed in this intake |
| Replica Skill | Claude Code skill suite for clean-room app recreation | [Jakeschincariol/replica-skill](https://github.com/Jakeschincariol/replica-skill) | MIT stated upstream |
| Claude Code Game Studios | Claude Code workflow for prototyping browser games | [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | MIT stated upstream |
| Huashu Design | Cross-agent design skills for deliverable visual assets and prototypes | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | MIT stated upstream; README says license changed to MIT on 2026-05-14 |
| PixelFX | Pixel-art effects library, gallery and coding-agent skill | [patch-gg/pixelfx](https://github.com/patch-gg/pixelfx) | Repository identity and README reviewed; license not confirmed in this intake |
| CLI-Anything | Framework for generating software-specific CLI harnesses so AI agents can operate existing applications | [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) | Apache-2.0 stated upstream |

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

## Gentle-AI

- **Project link:** [Official source](https://github.com/Gentleman-Programming/gentle-ai)

- **Type / Classification:** Deterministic engineering environment, skills and workflows for coding agents.

- **Purpose / Capabilities:** The README describes a cross-platform engineering environment for 18 agent hosts. It packages deterministic workflows, reusable skills and setup conventions around agents the user already operates.

- **Installation / Requirements:** Install and configure through the repository's documented setup; supported hosts and platform-specific steps are maintained upstream.

- **License / Cost:** MIT, as stated by the repository. No hands-on installation or behavior testing was performed.

- **Privacy / Security / Limitations:** Its deterministic workflow claims are upstream descriptions, not independent guarantees. Review shell access, hooks, file permissions and model-provider routing before enabling it in a real repository.

## Google Agent Skills

- **Project link:** [Official source](https://github.com/google/skills)

- **Type / Classification:** Vendor-authored Agent Skills collection for Google products and technologies.

- **Purpose / Capabilities:** Provides task-specific skills for Google products and technologies, including Google Cloud, IAM, onboarding and solution architecture. It is a collection of instructions, not a standalone agent.

- **Installation / Requirements:** Install with `npx skills add google/skills`; Node.js/npm/npx are required. Select individual skills and target agent during installation.

- **License / Cost:** Repository license was not separately confirmed in this intake. Inspect each skill's scripts, external services and Google Cloud permissions.

- **Privacy / Security / Limitations:** Useful for Google-stack workflows. Cloud skills may require an authenticated Google Cloud account and billable resources; a skill does not grant free cloud usage.

## Agent Skills Specification

- **Project link:** [Official source](https://github.com/agentskills/agentskills)

- **Type / Classification:** Open format/specification for portable agent skills.

- **Purpose / Capabilities:** Defines a lightweight folder-based format centered on `SKILL.md` metadata and instructions, with optional scripts, references, assets and templates. It aims to make skills portable across compatible agents.

- **Installation / Requirements:** Use the specification and validate host support; a skill folder is not guaranteed to work identically in every agent.

- **License / Cost:** Check the repository's current license and the licenses of individual skill contents separately.

- **Privacy / Security / Limitations:** Useful as an interoperability reference when authoring or reviewing skills. Host-specific tool support and execution permissions still differ.

## Vercel Skills CLI

- **Project link:** [Official source](https://github.com/vercel-labs/skills)

- **Type / Classification:** CLI for discovering and installing skills from the open agent-skills ecosystem.

- **Purpose / Capabilities:** Provides a CLI to discover, add, inspect and manage reusable agent skills from repositories and the skills.sh ecosystem. README lists support for many agent hosts.

- **Installation / Requirements:** Node.js/npm environment; install and usage commands are documented in the repository and npm package.

- **License / Cost:** MIT, as stated upstream. Skill repositories installed through the CLI retain their own licenses.

- **Privacy / Security / Limitations:** The CLI is an installer/discovery tool, not a guarantee that every third-party skill is safe or compatible. Review skill files before installation.

## Cursor Plugins

- **Project link:** [Official source](https://github.com/cursor/plugins)

- **Type / Classification:** Official Cursor plugin collection.

- **Purpose / Capabilities:** Collection of Cursor plugins for developer tools, frameworks and SaaS integrations. Each plugin is maintained in its own directory with a `.cursor-plugin/plugin.json` manifest.

- **Installation / Requirements:** Install through Cursor's plugin surfaces or follow each plugin's own instructions.

- **License / Cost:** Check the repository and individual plugin/dependency licenses before redistribution or commercial reuse.

- **Privacy / Security / Limitations:** Plugin permissions and connected services differ. Review each plugin's tools, network access and credentials rather than treating the collection as one homogeneous package.

## Jakub Krehel Skills

- **Project link:** [Official source](https://github.com/jakubkrehel/skills)

- **Type / Classification:** Agent skills for interface design and design engineering.

- **Purpose / Capabilities:** Provides skills for interface review, UI polish, typography, color, accessibility, layout and product writing.

- **Installation / Requirements:** Install with `npx skills add jakubkrehel/skills` and select compatible agent hosts.

- **License / Cost:** License not confirmed from the README excerpt; inspect the current LICENSE and individual assets before reuse.

- **Privacy / Security / Limitations:** Useful as design-review guidance, not a substitute for user research, accessibility testing or browser-based QA.

## Unslop

- **Project link:** [Official source](https://github.com/heydamir/unslop)

- **Type / Classification:** Design-oriented agent skill for improving AI-generated interfaces.

- **Purpose / Capabilities:** Reviews and refines AI-generated interfaces by identifying generic visual patterns and applying a more coherent product-specific design direction.

- **Installation / Requirements:** README documents installation for Claude Code and Codex; supports common web stacks and can work from a live URL where access permits.

- **License / Cost:** License not confirmed in this intake; check upstream LICENSE before reuse.

- **Privacy / Security / Limitations:** Generated changes still need visual, responsive, accessibility and functional review. A live-site URL may expose private pages or require authenticated browser access.

## Replica Skill

- **Project link:** [Official source](https://github.com/Jakeschincariol/replica-skill)

- **Type / Classification:** Claude Code skill suite for clean-room app recreation.

- **Purpose / Capabilities:** An eleven-skill workflow separates app reconnaissance, planning, design-system reconstruction, implementation, testing, branding and launch preparation. README explicitly frames the goal as recreating functionality, not copying proprietary code or assets.

- **Installation / Requirements:** Install from the repository or its Claude Code plugin marketplace instructions.

- **License / Cost:** MIT, as stated upstream.

- **Privacy / Security / Limitations:** Use clean-room practices. Do not copy protected source code, logos, text, user data or proprietary assets; verify rights before reproducing distinctive functionality.

## Claude Code Game Studios

- **Project link:** [Official source](https://github.com/Donchitos/Claude-Code-Game-Studios)

- **Type / Classification:** Claude Code workflow for prototyping browser games.

- **Purpose / Capabilities:** Guides an agent through clarifying a game idea, writing a one-page brief and building a playable browser-game prototype in iterative steps.

- **Installation / Requirements:** Open a copy of the repository in Claude Code and use its documented game-prototyping command/workflow.

- **License / Cost:** MIT, as stated upstream.

- **Privacy / Security / Limitations:** Generated game code and assets need testing. Review any downloaded assets, external libraries and deployment secrets independently.

## Huashu Design

- **Project link:** [Official source](https://github.com/alchaincyf/huashu-design)

- **Type / Classification:** Cross-agent design skills for deliverable visual assets and prototypes.

- **Purpose / Capabilities:** A design skill collection for producing product-launch animations, interactive prototypes, editable presentations, infographics and social-media graphics. README describes reusable style directions and templates.

- **Installation / Requirements:** Install with `npx skills add alchaincyf/huashu-design`; README lists Claude Code, Cursor, Codex, OpenClaw and Hermes.

- **License / Cost:** MIT, according to the current README; verify asset/template notices independently.

- **Privacy / Security / Limitations:** Output quality and time claims are upstream-reported. Review generated assets, font/image licenses and editable-file integrity before commercial publication.

## PixelFX

- **Project link:** [Official source](https://github.com/patch-gg/pixelfx)

- **Type / Classification:** Pixel-art effects library, gallery and coding-agent skill.

- **Purpose / Capabilities:** Contains hundreds of small pixel-art effects and animations, a browser gallery/export workflow, and a Claude Code skill for drafting and refining new effects.

- **Installation / Requirements:** Use the hosted gallery or follow repository instructions to integrate effects and export sprite sheets for a game engine.

- **License / Cost:** License not confirmed in this intake; check code, sprite and asset-specific terms before reuse.

- **Privacy / Security / Limitations:** Useful for prototyping game effects. Verify attribution and asset rights; generated effects should be reviewed in the target engine and frame rate.

## CLI-Anything

- **Project link:** [Official source](https://github.com/HKUDS/CLI-Anything)

- **Type / Classification:** Framework for generating software-specific CLI harnesses so AI agents can operate existing applications.

- **Purpose / Capabilities:** Generates CLI harnesses for existing desktop and professional software, making application functions available to agents through structured commands and JSON-oriented workflows. The repository includes a community CLI registry/hub and example integrations across creative and productivity applications.

- **Installation / Requirements:** Python 3.10+ and Click 8+ are listed. Install with the documented Python/pip workflow; CLI-Hub instructions are maintained in the repository.

- **License / Cost:** Apache-2.0, confirmed from the upstream LICENSE file.

- **Privacy / Security / Limitations:** Generated CLIs can invoke powerful operations in target applications. Review generated command schemas, filesystem/network effects and destructive operations before exposing them to an agent; the project's test counts and app coverage are upstream-reported.

## 📝 Note For Reader

Check the official project source for current requirements, permissions, pricing and license terms before installation or use.
