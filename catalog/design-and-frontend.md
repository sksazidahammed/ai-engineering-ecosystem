# Design and Frontend

**Catalogue version:** 1.16
**Last updated:** 2026-11-13 18:24 IST (UTC+05:30)

| Project | Provisional classification | Source | Status |
|---|---|---|---|
| UI UX Pro Max | Design-intelligence skill with searchable styles, rules and CLI | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | Verified identity; framework compatibility and coverage need checking |
| Taste Skill | Design-oriented agent skill for professional website and interface implementation | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | Verified identity; MIT stated upstream |
| Archify | Agent skill that turns prompts and plans into interactive HTML visualizations | [tt-a1i/archify](https://github.com/tt-a1i/archify) | Verified identity; Apache-2.0 stated upstream |
| Impeccable | Design vocabulary and critique/audit commands for coding agents | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | Verified identity; strongest for iterative interface refinement |
| PPT Master | AI-assisted native PowerPoint generation from documents | [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) | Verified identity; MIT stated upstream |
| Diagram Design | Agent skill for branded HTML/SVG diagrams | [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | Verified identity; MIT stated upstream |
| Aria Icons | Searchable icon catalogue, CLI and MCP server for coding agents | [LeulAria/Aria-Icons](https://github.com/LeulAria/Aria-Icons) | MIT code; individual icon collections retain their own licenses |
| Astryx | Customizable React design system built with StyleX | [meta/astryx](https://github.com/meta/astryx) | MIT stated upstream; project is currently described as beta |
| DesignCraft | Native desktop publishing and page-layout application | [storytold/designcraft](https://github.com/storytold/designcraft) | License not confirmed in this intake |
| Hallmark | Design skill for reducing generic AI-generated interface patterns | [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | Existing record; README reviewed; license details should be rechecked |
| Rune | Native GPU-rendered Rust UI framework with headless agent workflows | [anomalyco/rune](https://github.com/anomalyco/rune) | License not confirmed in this intake |

## UI UX Pro Max

- **Project link:** [Official source](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)

- **Type:** Design-intelligence skill and CLI for coding agents.

- **Purpose:** Provides searchable design styles, interface patterns, reasoning rules and implementation guidance that an agent can use while building or refining a UI.

- **Workflow:** The repository describes searching its design knowledge base and applying recommendations to supported frontend stacks. Exact framework coverage and current style/rule counts should be checked against the upstream README.

- **Assessment:** Useful as a structured design reference, not a guarantee of good UX. Review generated layouts for accessibility, responsiveness, consistency and compatibility with the existing design system.

## Taste Skill

- **Project link:** [Official source](https://github.com/Leonxlnx/taste-skill)

- **Type:** Design-oriented agent skill for professional website and interface implementation.

- **Purpose:** Supplies reusable design direction and implementation guidance to a compatible coding agent. The upstream project also references a related TasteCode desktop product; distinguish the skill repository from that separate application.

- **License:** MIT, as stated upstream.

- **Assessment:** Useful as a design brief and implementation aid. Inspect the skill instructions and evaluate the resulting interface rather than assuming that a visual style prompt ensures accessibility, responsiveness or maintainability.

## Archify

- **Project link:** [Official source](https://github.com/tt-a1i/archify)

- **Type:** Agent skill / visualization workflow for turning prompts and plans into interactive HTML outputs.

- **Purpose:** Generates visual explanations such as diagrams, maps and structured interactive presentations from supplied information.

- **License:** Apache-2.0, as stated upstream.

- **Assessment:** Useful for turning abstract information into navigable visuals. Check generated HTML, external assets, scripts and any third-party hosted or paid service separately.

## Impeccable

- **Project link:** [Official source](https://github.com/pbakaus/impeccable)

- **Type:** Design vocabulary and critique/audit command set for coding agents.

- **Purpose:** Helps agents reason about interface design, apply consistent design language, and review existing interfaces for visual, accessibility and performance issues.

- **Best use:** Iterative refinement of an existing product interface. It provides design guidance and workflows; it does not guarantee a coherent design system or production-quality implementation.

- **Practical checks:** Review generated code, responsive layouts, accessibility, semantic HTML and compatibility with the project's existing design system.

## PPT Master

- **Project link:** [Official source](https://github.com/hugohe3/ppt-master)

- **Type:** AI-assisted native PowerPoint generation workflow.

- **Purpose:** Uses source documents as input for creating editable PowerPoint presentations rather than returning only a flat slide image or PDF.

- **License:** MIT, as stated upstream.

- **Practical considerations:** Review slide structure, factual accuracy, visual hierarchy, fonts, charts and image rights. Model/API costs and document handling depend on the configured workflow.

## Diagram Design

- **Project link:** [Official source](https://github.com/cathrynlavery/diagram-design)

- **Type:** Agent skill for generating branded HTML/SVG diagrams.

- **Purpose:** Produces self-contained visual diagrams and adapts them to a supplied brand style. The README advertises a library of 45 diagram types; treat that number as an upstream-maintained claim.

- **License:** MIT, as stated upstream.

- **Practical considerations:** Validate diagram semantics, legibility, accessibility, SVG/HTML output and rendering at the intended display size.

## Aria Icons

- **Project link:** [Official source](https://github.com/LeulAria/Aria-Icons)

- **Type:** Icon discovery and integration toolkit comprising a searchable icon catalogue, npm CLI, REST API and MCP server.

- **Capabilities:** Searches icon collections, retrieves SVG or framework source, writes icon files into a project, maps imports between icon sets, audits mixed icon libraries and suggests a consistent collection.

- **Installation:** The README documents `npx -y aria-icons@latest setup`, Bun alternatives and global npm installation. The setup command can configure local MCP access for supported coding agents; a remote HTTP MCP endpoint is also documented.

- **Technology:** The repository is a Bun/TypeScript monorepo with a Next.js website, CLI package and API layer. Icon sources include vendored sets, theSVG brand logos and Iconify collections.

- **License:** MIT applies to the repository's code. The icon assets do not share one universal license: each upstream collection may have MIT, Apache, CC0, attribution, copyleft or other terms. Check collection metadata and attribution requirements before shipping icons.

- **Assessment:** Useful for consistent icon discovery and agent-assisted insertion. Do not treat the MIT code license as permission to redistribute every icon asset without checking its source license.

## Astryx

- **Project link:** [Official source](https://github.com/meta/astryx)

- **Type / Classification:** Customizable React design system built with StyleX.

- **Purpose / Capabilities:** A customizable design system for React applications, built on React 19+ and StyleX, with documentation, Storybook and an interactive sandbox.

- **Installation / Requirements:** Use the npm package and current documentation; React 19+ is stated upstream. Review beta API stability before adopting it.

- **License / Cost:** MIT stated upstream; verify package and asset notices as applicable.

- **Privacy / Security / Limitations:** Beta APIs may change. Validate accessibility, theming, bundle impact and component behavior against the target product.

## DesignCraft

- **Project link:** [Official source](https://github.com/storytold/designcraft)

- **Type / Classification:** Native desktop publishing and page-layout application.

- **Purpose / Capabilities:** A Rust-based desktop publishing and page-layout studio for creating and arranging publication layouts, with native desktop builds and a WebAssembly browser version.

- **Installation / Requirements:** Check current release downloads and platform requirements in the repository and official ArtCraft site.

- **License / Cost:** License not confirmed in this intake; inspect bundled fonts, templates and assets separately.

- **Privacy / Security / Limitations:** Do not confuse this with an AI design skill: it is a page-layout application. Verify export fidelity and print-production requirements before professional use.

## Hallmark

- **Project link:** [Official source](https://github.com/Nutlope/hallmark)

- **Type / Classification:** Design skill for reducing generic AI-generated interface patterns.

- **Purpose / Capabilities:** A design skill for Claude Code, Codex, Cursor and OpenCode. It applies theme selection, layout guidance and browser-based lint/review gates to reduce common AI-generated design patterns.

- **Installation / Requirements:** Install using the current upstream instructions and a compatible coding agent; browser-based review requires the documented browser tooling.

- **License / Cost:** Existing catalogue record retained; confirm current LICENSE before reuse.

- **Privacy / Security / Limitations:** A design skill cannot guarantee good design or factual accuracy. Keep accessibility, responsive behavior and functional testing as independent release gates.

## Rune

- **Project link:** [Official source](https://github.com/anomalyco/rune)

- **Type / Classification:** Native GPU-rendered Rust UI framework with headless agent workflows.

- **Purpose / Capabilities:** A cross-platform UI framework with its own renderer, layout, text and animation systems. Apps can run headlessly so agents can render screenshots, inspect element trees and drive scripted input.

- **Installation / Requirements:** Rust toolchain and platform-specific graphics dependencies; follow upstream build and example instructions.

- **License / Cost:** License not confirmed in this intake.

- **Privacy / Security / Limitations:** Headless rendering can support UI-agent testing, but it is not a complete browser automation system. Validate platform support, accessibility and rendering stability.

## 📝 Note For Reader

Design-related agent skills can generate code/, modify application structure, or introduce dependencies. Evaluate the quality of generated output, accessibility, responsive behavior, design-system compatibility, and license constraints. A visually convincing demo is not proof of production readiness.
