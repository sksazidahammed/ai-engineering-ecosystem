# Coding and Development

**Catalogue version:** 1.0  
**Last updated:** 2026-11-12 17:39 IST (UTC+05:30)

| Project | Provisional classification | Source | Status |
|---|---|---|---|
| Superpowers | Agent skills / development workflow | [Repository](https://github.com/obra/superpowers) | Candidate — review pending |
| Matt Pocock Skills | Agent skills | [Repository](https://github.com/mattpocock/skills) | Candidate — review pending |
| Everything Claude Code (ECC) | Coding-agent configuration / skills | [Repository](https://github.com/affaan-m/ECC) | Candidate — review pending |
| Karpathy-Inspired Skills | Claude Code plugin / agent instruction pack; includes Cursor project rule | [Repository](https://github.com/multica-ai/andrej-karpathy-skills) | Verified identity; provenance note applies |
| Ponytail | Exact identity needs confirmation | [Submitted repository](https://github.com/DietrichGebert/ponytail) | Candidate — review pending |
| Anthropic Agent Skills | Agent skills collection | [Official repository](https://github.com/anthropics/skills) | Verified identity; details review pending |

## Karpathy-Inspired Skills

- **Repository:** [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)
- **Type:** Claude Code plugin / reusable agent-instruction pack; also includes a Cursor project rule.
- **Purpose:** Reduce common coding-agent failure modes through four principles: think before coding, simplicity first, surgical changes, and goal-driven execution with verifiable success criteria.
- **Installation modes:** Claude Code marketplace plugin or a project-level `CLAUDE.md`; Cursor support is provided through a committed project rule.
- **License:** MIT, as stated in the repository.
- **Provenance caution:** The README's Claude Code marketplace and raw-file installation examples reference `forrestchang/andrej-karpathy-skills`, not the submitted `multica-ai` owner. Confirm the intended canonical source and current plugin instructions before installing.
- **Practical assessment:** A compact, low-friction instruction set for reducing overengineering and unintended edits. It is guidance, not a guarantee of correctness, and it does not replace tests, code review, or explicit project-specific requirements.

## Editorial notes

This category is intended for tools that directly support software development, coding-agent behavior, repository workflows, and engineering practices. Skills are not the same thing as standalone applications or agent frameworks. The classification will be refined after checking each project's current README, supported agents, installation method, license, and maintenance signals.

Do not install a skill into a production coding agent solely on the basis of its name. Review its instructions and scripts first.
