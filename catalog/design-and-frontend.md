# Design and Frontend

**Catalogue version:** 1.6  
**Last updated:** 2026-11-12 19:50 IST (UTC+05:30)

| Project | Provisional classification | Source | Status |
|---|---|---|---|
| UI UX Pro Max | Design-intelligence skill with searchable styles, rules and CLI | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | Verified identity; framework compatibility and coverage need checking |
| Taste Skill | Design-oriented agent skill for professional website and interface implementation | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | Verified identity; MIT stated upstream |
| Archify | Agent skill that turns prompts and plans into interactive HTML visualizations | [tt-a1i/archify](https://github.com/tt-a1i/archify) | Verified identity; Apache-2.0 stated upstream |
| Impeccable | Design vocabulary and critique/audit commands for coding agents | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | Verified identity; strongest for iterative interface refinement |
| PPT Master | AI-assisted native PowerPoint generation from documents | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | Verified identity; MIT stated upstream |
| Diagram Design | Agent skill for branded HTML/SVG diagrams | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | Verified identity; MIT stated upstream |

## Impeccable

- **Repository:** [pbakaus/impeccable](https://github.com/pbakaus/impeccable)
- **Type:** Design vocabulary and critique/audit command set for coding agents.
- **Purpose:** Helps agents reason about interface design, apply consistent design language, and review existing interfaces for visual, accessibility and performance issues.
- **Best use:** Iterative refinement of an existing product interface. It provides design guidance and workflows; it does not guarantee a coherent design system or production-quality implementation.
- **Practical checks:** Review generated code, responsive layouts, accessibility, semantic HTML and compatibility with the project's existing design system.

## Taste Skill

- **Repository:** [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)
- **Type:** Design-oriented agent skill for producing polished websites and user interfaces.
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
## Reader notes

Design-related agent skills can generate code, modify application structure, or introduce dependencies. Evaluate the quality of generated output, accessibility, responsive behavior, design-system compatibility, and license constraints. A visually convincing demo is not proof of production readiness.
