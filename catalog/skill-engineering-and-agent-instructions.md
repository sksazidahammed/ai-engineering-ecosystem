# Skill Engineering and Agent Instructions

**Directory version:** 1.16  
**Last updated:** 2026-11-13 18:24 IST (UTC+05:30)

| Project | Classification | Official source | Status |
|---|---|---|---|
| book-to-skill | Document-to-skill generation CLI | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | MIT stated in README |
| Cangjie Skill | Knowledge-to-skill distillation toolkit | [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill) | MIT stated in README |
| SkillOpt | Research framework for optimizing agent skills | [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt) | MIT stated in README |
| agents-best-practices | Provider-neutral agent-harness design skill | [DenisSergeevitch/agents-best-practices](https://github.com/DenisSergeevitch/agents-best-practices) | MIT stated in README |
| benjamin-plus | Token-efficiency skill for coding agents | [JetBrains/benjamin-plus-skill](https://github.com/JetBrains/benjamin-plus-skill) | Upstream reports token/cost reductions |
| writing-for-agents | Sub-skill: writing-for-agents | [mattpocock/skills](https://github.com/mattpocock/skills) | Use the parent repository's installation and license information |
| wayfinder | Sub-skill: Wayfinder | [mattpocock/skills](https://github.com/mattpocock/skills) | Parent-repository license and install instructions apply |
| grill-with-docs | Sub-skill: documentation-led requirements discovery | [mattpocock/skills](https://github.com/mattpocock/skills) | Not a separate repository record |
| agents-best-practices | Agent design and harness guidance | [DenisSergeevitch/agents-best-practices](https://github.com/DenisSergeevitch/agents-best-practices) | MIT stated upstream |

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

- **Type / Classification:** Provider-neutral agent-harness design skill.

- **Purpose:** A reusable skill for designing, auditing, refactoring and explaining reliable agent harnesses across domains.

- **Workflow / Requirements:** README documents installation through the Skills CLI or manual skill directories for Codex and Claude Code.

- **License / Cost / Status:** MIT stated in README; generated architectures still need security and operational review.

## benjamin-plus

- **Project link:** [Official source](https://github.com/JetBrains/benjamin-plus-skill)

- **Type / Classification:** Token-efficiency skill for coding agents.

- **Purpose:** Encourages efficient repository reconnaissance, bounded file reads, batched environment checks and sensible polling.

- **Workflow / Requirements:** Distributed as an agent skill; detailed rules are in the repository's RULESET.md.

- **License / Cost / Status:** Upstream reports token/cost reductions; treat them as maintainer measurements, not independent benchmarks.

## writing-for-agents

- **Project link:** [Official source](https://github.com/mattpocock/skills)

- **Type / Classification:** Sub-skill: writing-for-agents.

- **Purpose:** A skill within Matt Pocock's larger skills repository for writing content intended to be consumed by agents.

- **Workflow / Requirements:** This is a file/subdirectory within the already-catalogued mattpocock/skills repository, not a separate repository record.

- **License / Cost / Status:** Use the parent repository's installation and license information; do not count this path as a distinct project.

## wayfinder

- **Project link:** [Official source](https://github.com/mattpocock/skills)

- **Type / Classification:** Sub-skill: Wayfinder.

- **Purpose:** A spec/planning-oriented skill within Matt Pocock's larger engineering skills collection.

- **Workflow / Requirements:** This is a subdirectory of the existing Matt Pocock Skills record, not an independent repository.

- **License / Cost / Status:** Parent-repository license and install instructions apply; skill-specific behavior should be reviewed at the linked path.

## grill-with-docs

- **Project link:** [Official source](https://github.com/mattpocock/skills)

- **Type / Classification:** Sub-skill: documentation-led requirements discovery.

- **Purpose:** A skill in Matt Pocock Skills for interrogating and clarifying requirements before implementation.

- **Workflow / Requirements:** The submitted URL points to a subdirectory of an existing repository; it is cross-listed conceptually under spec-driven development.

- **License / Cost / Status:** Not a separate repository record; follow the parent project's current setup.

## agents-best-practices

- **Project link:** [Official source](https://github.com/DenisSergeevitch/agents-best-practices)

- **Type / Classification:** Agent design and harness guidance.

- **Purpose:** Provides reusable practices for agent workflows beyond coding, including authorization, execution, recording and feedback loops.

- **Workflow / Requirements:** README identifies a portable Agent Skill compatible with Codex and Claude Code.

- **License / Cost / Status:** MIT stated upstream; examples are guidance, not a substitute for threat modelling or policy controls.

## 📝 Note For Reader

Entries are categorized by their primary use. A repository README review verifies the submitted identity and upstream-described scope; it does not constitute hands-on installation, performance, security or legal testing. Recheck current upstream documentation, license files and provider terms before deployment.
