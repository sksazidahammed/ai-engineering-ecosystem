# Security Review and Agent Guardrails

**Directory version:** 1.16  
**Last updated:** 2026-11-13 18:24 IST (UTC+05:30)

| Project | Classification | Official source | Status |
|---|---|---|---|
| Strix | Autonomous AI application penetration-testing tool | [usestrix/strix](https://github.com/usestrix/strix) | Apache-2.0 stated in README |
| Reverse Skill | Cybersecurity and reverse-engineering skill router | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | Use only on software and systems you are authorized to analyze |
| HexStrike AI | MCP cybersecurity automation platform | [0x4m4/hexstrike-ai](https://github.com/0x4m4/hexstrike-ai) | MIT stated in README |
| Vercel DeepSec | Agent-powered source-code vulnerability scanner | [vercel-labs/deepsec](https://github.com/vercel-labs/deepsec) | Apache-2.0 stated in README |
| Trail of Bits Skills | Security-analysis plugin and skill marketplace | [trailofbits/skills](https://github.com/trailofbits/skills) | Review each plugin's code, tools and license individually |
| Garak | LLM vulnerability scanner and red-team toolkit | [NVIDIA/garak](https://github.com/NVIDIA/garak) | Apache-2.0 stated in README |
| OpenCodeReview | Automated code-review system | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | Review data access and model-provider processing |
| Destructive Command Guard | Pre-execution destructive-command guard | [Dicklesworthstone/destructive_command_guard](https://github.com/Dicklesworthstone/destructive_command_guard) | Custom license stated upstream |
| React Doctor | Deterministic React project auditor | [millionco/react-doctor](https://github.com/millionco/react-doctor) | Check the current package license and rule behavior |
| tuicr | Terminal code-review interface | [agavra/tuicr](https://github.com/agavra/tuicr) | Review tokens and permissions before connecting hosted repositories |

## Strix

- **Project link:** [Official source](https://github.com/usestrix/strix)

- **Type / Classification:** Autonomous AI application penetration-testing tool.

- **Purpose:** Runs agent-driven security testing to identify and help fix application vulnerabilities.

- **Workflow / Requirements:** README links documentation, a Python package and an optional hosted cloud product.

- **License / Cost / Status:** Apache-2.0 stated in README; test only systems you own or are explicitly authorized to assess.

## Reverse Skill

- **Project link:** [Official source](https://github.com/zhaoxuya520/reverse-skill)

- **Type / Classification:** Cybersecurity and reverse-engineering skill router.

- **Purpose:** A collection/router of security skills for reverse engineering and related analysis workflows.

- **Workflow / Requirements:** README identifies a versioned skill package and MIT license badge.

- **License / Cost / Status:** Use only on software and systems you are authorized to analyze; inspect individual skill actions before installation.

## HexStrike AI

- **Project link:** [Official source](https://github.com/0x4m4/hexstrike-ai)

- **Type / Classification:** MCP cybersecurity automation platform.

- **Purpose:** Connects AI agents to a large collection of security tools and autonomous testing workflows.

- **Workflow / Requirements:** README advertises Python 3.8+, MCP compatibility and a multi-agent toolset.

- **License / Cost / Status:** MIT stated in README; high-impact dual-use capability. Isolate the environment and restrict targets to authorized scope.

## Vercel DeepSec

- **Project link:** [Official source](https://github.com/vercel-labs/deepsec)

- **Type / Classification:** Agent-powered source-code vulnerability scanner.

- **Purpose:** Scans large repositories for hard-to-find vulnerabilities and can distribute analysis across worker machines.

- **Workflow / Requirements:** README warns that large scans may cost thousands or tens of thousands of dollars in model usage.

- **License / Cost / Status:** Apache-2.0 stated in README; model/API cost can be substantial. Review source-code data flow and run only on authorized repositories.

## Trail of Bits Skills

- **Project link:** [Official source](https://github.com/trailofbits/skills)

- **Type / Classification:** Security-analysis plugin and skill marketplace.

- **Purpose:** Provides installable security analysis, testing and development plugins for Claude Code, Codex and supported workspace marketplaces.

- **Workflow / Requirements:** README documents marketplace installation and lists specialist plugins.

- **License / Cost / Status:** Review each plugin's code, tools and license individually; marketplace membership is not a security certification.

## Garak

- **Project link:** [Official source](https://github.com/NVIDIA/garak)

- **Type / Classification:** LLM vulnerability scanner and red-team toolkit.

- **Purpose:** Probes LLM-backed applications for failures such as prompt injection, data leakage, jailbreaks, misinformation and unsafe outputs.

- **Workflow / Requirements:** README describes static, dynamic and adaptive probes and links documentation and test workflows.

- **License / Cost / Status:** Apache-2.0 stated in README; scanning can trigger unsafe outputs or external service calls—use controlled test targets.

## OpenCodeReview

- **Project link:** [Official source](https://github.com/alibaba/open-code-review)

- **Type / Classification:** Automated code-review system.

- **Purpose:** A code-review project with a dedicated website and npm distribution for review workflows.

- **Workflow / Requirements:** README links official docs/site, package and CI; inspect deployment and integration guides for current architecture.

- **License / Cost / Status:** Review data access and model-provider processing; verify the exact license in upstream LICENSE.

## Destructive Command Guard

- **Project link:** [Official source](https://github.com/Dicklesworthstone/destructive_command_guard)

- **Type / Classification:** Pre-execution destructive-command guard.

- **Purpose:** A hook for coding agents that blocks destructive commands before execution across multiple agent hosts.

- **Workflow / Requirements:** README lists integrations for Claude Code, Codex CLI, Gemini CLI, Copilot, Cursor and others.

- **License / Cost / Status:** Custom license stated upstream; inspect LICENSE. A guardrail is not a complete sandbox or guarantee against destructive actions.

## React Doctor

- **Project link:** [Official source](https://github.com/millionco/react-doctor)

- **Type / Classification:** Deterministic React project auditor.

- **Purpose:** Runs checks for React state/effect issues, performance, architecture, security, accessibility and maintainability.

- **Workflow / Requirements:** README documents `npx react-doctor` usage, agent skill installation and CI integration.

- **License / Cost / Status:** Check the current package license and rule behavior; automated findings need developer review.

## tuicr

- **Project link:** [Official source](https://github.com/agavra/tuicr)

- **Type / Classification:** Terminal code-review interface.

- **Purpose:** A vim-keybinding TUI for reviewing diffs and exporting comments to GitHub, GitLab, Gitea, Bitbucket, Azure DevOps, Gerrit or clipboard.

- **Workflow / Requirements:** README documents shell, Homebrew, Cargo, Nix and other installation routes.

- **License / Cost / Status:** Review tokens and permissions before connecting hosted repositories; inspect current LICENSE.

## 📝 Note For Reader

Entries are categorized by their primary use. A repository README review verifies the submitted identity and upstream-described scope; it does not constitute hands-on installation, performance, security or legal testing. Recheck current upstream documentation, license files and provider terms before deployment.
