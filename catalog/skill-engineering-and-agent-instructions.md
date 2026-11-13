# Skill Engineering and Agent Instructions

**Catalogue version:** 1.16  
**Last updated:** 2026-11-13 18:24 IST (UTC+05:30)

| Project | Classification | Official source | Status |
|---|---|---|---|
| book-to-skill | Document-to-skill generation CLI | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | MIT stated in README |
| Cangjie Skill | Knowledge-to-skill distillation toolkit | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | MIT stated in README |
| SkillOpt | Research framework for optimizing agent skills | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | MIT stated in README |
| agents-best-practices | Provider-neutral agent-harness design skill | [DenisSergeevitch/agents-best-practices](https://github.com/DenisSergeevitch/agents-best-practices) | MIT stated in README |
| benjamin-plus | Token-efficiency skill for coding agents | [JetBrains/benjamin-plus-skill](https://github.com/JetBrains/benjamin-plus-skill) | Upstream reports token/cost reductions |
| OpenSpace | Skill-building / agent capability research candidate | [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) | Repository README could not be fetched; verification pending |
| Claude Code Templates | Installable catalogue of Claude Code agents, commands, hooks, plugins and templates | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | MIT stated in README; component compatibility varies |


## book-to-skill

- **Project link:** [Official source](https://github.com/virgiliojr94/book-to-skill)

- **Type / Classification:** Document-to-skill generation CLI.

- **Purpose:** Converts technical books, document folders and source collections into reusable agent skills for multiple coding agents.

- **Workflow / Requirements:** The README lists PDF, EPUB, DOCX, Markdown, HTML, RTF and MOBI inputs and multiple agent hosts.

- **License / Cost / Status:** MIT stated in README; conversion quality and source rights remain the user's responsibility.

## Cangjie Skill

- **Project link:** [Official source](https://github.com/kangarooking/cangjie-skill)

- **Type / Classification:** Knowledge-to-skill distillation toolkit.

- **Purpose:** Distils methods from books, long-form video and podcasts into callable agent skills using a structured extraction and compilation workflow.

- **Workflow / Requirements:** README describes a local Python toolchain, capability bundles, single-skill or pack outputs, evaluation and rollback.

- **License / Cost / Status:** MIT stated in README; verify source permissions and review generated skill behavior.

## SkillOpt

- **Project link:** [Official source](https://github.com/microsoft/SkillOpt)

- **Type / Classification:** Research framework for optimizing agent skills.

- **Purpose:** Treats skill text and workflows as optimizable artifacts, using iterative training/evaluation concepts without changing model weights.

- **Workflow / Requirements:** The project provides Python tooling, documentation, a paper and reproduction guidance.

- **License / Cost / Status:** MIT stated in README; research results and performance claims require independent reproduction.

## agents-best-practices

- **Project link:** [Official source](https://github.com/DenisSergeevitch/agents-best-practices)

- **Type / Classification:** Agent design and harness guidance.

- **Purpose:** Provides reusable practices for agent workflows beyond coding, including authorization, execution, recording and feedback loops.

- **Workflow / Requirements:** README identifies a portable Agent Skill compatible with Codex and Claude Code.

- **License / Cost / Status:** MIT stated upstream; examples are guidance, not a substitute for threat modelling or policy controls.

## benjamin-plus

- **Project link:** [Official source](https://github.com/JetBrains/benjamin-plus-skill)

- **Type / Classification:** Token-efficiency skill for coding agents.

- **Purpose:** Encourages efficient repository reconnaissance, bounded file reads, batched environment checks and sensible polling.

- **Workflow / Requirements:** Distributed as an agent skill; detailed rules are in the repository's RULESET.md.

- **License / Cost / Status:** Upstream reports token/cost reductions; treat them as maintainer measurements, not independent benchmarks.

## OpenSpace

- **Project link:** [Official source](https://github.com/HKUDS/OpenSpace)

- **Type / Classification:** Skill-building and agent capability research candidate; exact classification remains provisional.

- **Purpose:** The repository was submitted in the skill-building section, but its actual scope could not be confirmed from an accessible upstream README during this intake.

- **Verification status:** README retrieval failed through the connected GitHub source. No capabilities, requirements or license are asserted until the repository can be inspected.

- **Assessment:** Retained as a verification-pending discovery record rather than excluded or described by guesswork.

## Claude Code Templates

- **Project link:** [Official source](https://github.com/davila7/claude-code-templates)

- **Type / Classification:** Installable catalogue and CLI for Claude Code components.

- **Purpose:** Collects and distributes Claude Code agents, commands, hooks, plugins and related configuration templates.

- **Workflow / Requirements:** README describes an npm CLI for browsing and installing selected components, with a companion web catalogue and documentation.

- **License / Cost:** MIT stated in README; individual third-party dependencies and external services may have separate terms.

- **Security / Limitations:** Components can add executable hooks, tools and agent permissions. Inspect each component and its source before installing it into a sensitive project.

## 📝 Note For Reader

Entries are categorized by their primary use. A repository README review verifies the submitted identity and upstream-described scope; it does not constitute hands-on installation, performance, security or legal testing. Recheck current upstream documentation, license files and provider terms before deployment.
