# Taxonomy migration: 24 categories → 13

Based on catalogue v1.16 as read from `MASTER-CATALOG.md`. Placements are judgement calls from each record's description; review before applying. `taxonomy/taxonomy.yml` is the source of truth going forward.

## 1. Default mapping

| Old category | New category (default) | Exceptions (move instead to) |
|---|---|---|
| Coding and development | 03 Skills, plugins and instructions | Design skills (Jakub Krehel, Unslop, Huashu Design, PixelFX) → 08; CLI-Anything → 07 |
| Research and intelligence | 07 Research, browser and computer use | Graphify, Understand Anything, TokenEconomizer → 05; REA → 06; Career Ops, Repolyze → 13 |
| Agent frameworks and orchestration | 02 Multi-agent orchestration | Claude-Mem, Engram, GBrain, Headroom, Caveman → 05; GSD Core, BMAD → 04; AG2, OpenClaw, Cindy → 01 |
| Cybersecurity and security auditing | 06 Security and guardrails | OpenSSL: keep in 06 (`security-libraries`) or drop as out of scope — your call |
| Design and frontend | 08 Design, UI and visualization | — |
| Writing and content | 09 Media, writing and content | Deslop → 03 (`instruction-and-style-packs`) |
| Productivity and workflows | 13 Applications and utilities | Knowledge Work Plugins → 03; Harper → 09 |
| Media, audio and video | 09 Media, writing and content | — |
| Local AI and agent applications | 10 Models, inference and gateways | Hex → 09; Agent Desktop → 07; DSH Go, OpenMausBot → 01; watermark remover → 13 |
| Networking and system utilities | 13 Applications and utilities | abtop, Herdr, Worktrunk → 02; Gortex → 05 |
| AI project collections | 12 Learning and reference | — |
| Model infrastructure and gateways | 10 Models, inference and gateways | — |
| Data platforms and infrastructure | 11 Data, backend and infrastructure | — |
| Skill engineering and agent instructions | 03 Skills, plugins and instructions | — |
| Spec-driven development and planning | 04 Spec-driven development and planning | — |
| Code intelligence and context engineering | 05 Context, memory and code intelligence | — |
| Coding agent CLIs and harnesses | 01 Agent harnesses and runtimes | — |
| Agent workspaces and orchestration | 02 Multi-agent orchestration | — |
| Web research and browser automation | 07 Research, browser and computer use | — |
| Security review and agent guardrails | 06 Security and guardrails | — |
| Model gateways and agent integrations | 10 Models, inference and gateways | Desktop Commander MCP → 07; Corsair, AWS toolkit → 11 |
| Design engineering and visualization | 08 Design, UI and visualization | — |
| Media, device and mobile automation | split | Claude Video → 09; Agent Device → 07 |
| AI engineering reference and learning | 12 Learning and reference | — |

## 2. Scope decisions you need to make

Category 13 holds items that are not clearly "AI engineering": invoice builder, file converters, file-transfer tools, form builder, network utilities. Pick one rule and apply it to all of them:

- **Keep** only if AI-related or directly usable by an agent, or
- **Keep** everything and accept a broader "developer tools" scope.

Anything that fails the chosen rule is removed (its record can stay in git history).

## 3. Order of operations

1. Freeze the 13 categories in `taxonomy.yml`.
2. Convert records to one YAML file each in `data/records/`, using `unknown` / `unassessed` / `NOASSERTION` where a field is not yet checked.
3. Run `python scripts/validate.py` until clean.
4. Generate the README and category pages from the data, then retire the hand-edited tables.
5. Add scheduled CI for link checks and GitHub health checks (archived, last push, license).
