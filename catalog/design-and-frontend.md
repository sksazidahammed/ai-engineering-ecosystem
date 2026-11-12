# Design and Frontend

**Catalogue version:** 1.6  
**Last updated:** 2026-11-12 19:52 IST (UTC+05:30)

| Project | Provisional classification | Source | Status |
|---|---|---|---|
| UI UX Pro Max | Design-intelligence skill with searchable styles, rules and CLI | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | Verified identity; framework compatibility and coverage need checking |
| Taste Skill | Design-oriented agent skill for professional website and interface implementation | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | Verified identity; MIT stated upstream |
| Archify | Agent skill that turns prompts and plans into interactive HTML visualizations | [tt-a1i/archify](https://github.com/tt-a1i/archify) | Verified identity; Apache-2.0 stated upstream |
| Impeccable | Design vocabulary and critique/audit commands for coding agents | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | Verified identity; strongest for iterative interface refinement |
| PPT Master | AI-assisted native PowerPoint generation from documents | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | Verified identity; MIT stated upstream |
| Diagram Design | Agent skill for branded HTML/SVG diagrams | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | Verified identity; MIT stated upstream |

## UI UX Pro Max

- **Repository:** [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)
- **Type:** Design-intelligence skill and CLI for coding agents.
- **Purpose:** Provides searchable design styles, interface patterns, reasoning rules and implementation guidance that an agent can use while building or refining a UI.
- **Workflow:** The repository describes searching its design knowledge base and applying recommendations to supported frontend stacks. Exact framework coverage and current style/rule counts should be checked against the upstream README.
- **Assessment:** Useful as a structured design reference, not a guarantee of good UX. Review generated layouts for accessibility, responsiveness, consistency and compatibility with the existing design system.

## Taste Skill

- **Repository:** [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)
- **Type:** Design-oriented agent skill for professional website and interface implementation.
- **Purpose:** Supplies reusable design direction and implementation guidance to a compatible coding agent. The upstream project also references a related TasteCode desktop product; distinguish the skill repository from that separate application.
- **License:** MIT, as stated upstream.
- **Assessment:** Useful as a design brief and implementation aid. Inspect the skill instructions and evaluate the resulting interface rather than assuming that a visual style prompt ensures accessibility, responsiveness or maintainability.

## Archify

- **Repository:** [tt-a1i/archify](https://github.com/tt-a1i/archify)
- **Type:** Agent skill / visualization workflow for turning prompts and plans into interactive HTML outputs.
- **Purpose:** Generates visual explanations such as diagrams, maps and structured interactive presentations from supplied information.
- **License:** Apache-2.0, as stated upstream.
- **Assessment:** Useful for turning abstract information into navigable visuals. Check generated HTML, external assets, scripts and any third-party hosted or paid service separately.

## Impeccable

- **Repository:** [pbakaus/impeccable](https://github.com/pbakaus/impeccable)
- **Type:** Design vocabulary and critique/audit command set for coding agents.
- **Purpose:** Helps agents reason about interface design, apply consistent design language, and review existing interfaces for visual, accessibility and performance issues.
- **Best use:** Iterative refinement of an existing product interface. It provides design guidance and workflows; it does not guarantee a coherent design system or production-quality implementation.
- **Practical checks:** Review generated code, responsive layouts, accessibility, semantic HTML and compatibility with the project's existing design system.

## PPT Master

- **Repository:** [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master)
- **Type:** AI-assisted native PowerPoint generation workflow.
- **Purpose:** Uses source documents as input for creating editable PowerPoint presentations rather than returning only a flat slide image or PDF.
- **License:** MIT, as stated upstream.
- **Practical considerations:** Review slide structure, factual accuracy, visual hierarchy, fonts, charts and image rights. Model/API costs and document handling depend on the configured workflow.

## Diagram Design

- **Repository:** [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)
- **Type:** Agent skill for generating branded HTML/SVG diagrams.
- **Purpose:** Produces self-contained visual diagrams and adapts them to a supplied brand style. The README advertises a library of 45 diagram types; treat that number as an upstream-maintained claim.
- **License:** MIT, as stated upstream.
- **Practical considerations:** Validate diagram semantics, legibility, accessibility, SVG/HTML output and rendering at the intended display size.

## Reader notes

Design-related agent skills can generate code, modify application structure, or introduce dependencies. Evaluate the quality of generated output, accessibility, responsive behavior, design-system compatibility, and license constraints. A visually convincing demo is not proof of production readiness.
