# Agent Frameworks and Orchestration

**Catalogue version:** 1.10
**Last updated:** 2026-11-12 20:54 IST (UTC+05:30)

| Project | Provisional classification | Source | Status |
|---|---|---|---|
| gstack | Role-based engineering workflow and tool collection | [garrytan/gstack](https://github.com/garrytan/gstack) | Repository identity verified; MIT stated upstream |
| Caveman | Agent skill and proxy/runtime for token-efficient agent communication | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | Verified identity; split MIT/BSL-1.1 license |
| Claude-Mem | Persistent coding-agent memory and context system | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | Repository identity verified; inspect data retention and redaction |
| Headroom | Local context-compression middleware for prompts, tool outputs and agent history | [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | Verified identity; savings depend on workload and content |
| GSD Core | Spec-driven development and context-engineering workflow; successor to archived GSD repo | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | Successor identified; recheck current release and license |
| BMAD Method | Agile AI-driven development framework with role-based agents | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | Repository identity verified; stable v6 and preview v7 differ in maturity |
| MiroFish | Multi-agent swarm simulation / scenario exploration engine | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | Verified identity; predictive validity not established |

## gstack

- **Project link:** [Official source](https://github.com/garrytan/gstack)

- **Type:** Role-based engineering workflow and tool/skill collection for coding agents.

- **Roles and capabilities:** Packages product, design, engineering management, code review, QA, security and release responsibilities into reusable workflows.

- **Automation:** The README describes browser-driven QA and automated review flows.

- **Requirements:** Requires a compatible coding agent and local dependencies; some features have additional platform or toolchain prerequisites.

- **License:** MIT, as stated upstream.

- **Assessment:** Useful for simulating a cross-functional engineering team. Security checks and release automation are review aids, not approval to merge unreviewed changes.

## Caveman

- **Project link:** [Official source](https://github.com/JuliusBrussee/caveman)

- **Type:** Coding-agent skill with an optional proxy/runtime for token-efficient agent communication.

- **Purpose:** Rewrites conversational output into shorter forms while aiming to preserve code correctness.

- **Performance claims:** The README publishes benchmark results; treat them as upstream-reported until reproduced on your own workloads.

- **License:** Split licensing applies. Skill/adoption surfaces are MIT; engine-linked runtime components are BSL-1.1 source-available, with a future change date and commercial restrictions for third-party hosting.

- **Deployment caution:** Read the license for each component before deploying, modifying or redistributing the runtime.

- **Assessment:** Potentially useful for reducing token use, but validate that compression does not remove essential code, reasoning or safety context.

## Claude-Mem

- **Project link:** [Official source](https://github.com/thedotmack/claude-mem)

- **Type:** Persistent memory and context-retrieval system for coding agents.

- **Workflow:** Records session activity, compresses observations and retrieves relevant context in later sessions. The README documents support across multiple agents.

- **Requirements:** Uses a local worker/runtime and stores project or session context.

- **Privacy and security:** Review data retention, database location, redaction behavior and model/API configuration before using it with secrets or private repositories.

- **License:** Apache-2.0, as stated upstream.

- **Assessment:** Useful for continuity across coding sessions, provided stored context is managed as sensitive project data.

## Headroom

- **Project link:** [Official source](https://github.com/headroomlabs-ai/headroom)

- **Type:** Context-compression middleware for AI-agent workflows.

- **Inputs:** Can process prompts, tool outputs, logs, retrieval-augmented generation (RAG) chunks and conversation history.

- **Execution model:** Upstream describes local/in-process compression and reports token savings on selected workloads.

- **License:** Apache-2.0, as stated upstream.

- **Limitations:** Compression effectiveness varies by content. Validate semantic fidelity on your own tasks, especially code, logs and structured data.

- **Assessment:** Useful where context size and inference cost are constraints, but compression must not discard critical instructions or evidence.

## GSD Core

- **Project link:** [Official source](https://github.com/open-gsd/gsd-core)

- **Type:** Spec-driven development and context-engineering workflow; listed here through the successor project.

- **Repository history:** The submitted `gsd-build/get-shit-done` repository is archived and explicitly points to `open-gsd/gsd-core` as its active successor.

- **Catalogue treatment:** This entry links to the successor, not the archived repository.

- **Installation and license:** Re-check the successor's current setup instructions, release status and license before adopting it. Do not rely on old installation instructions from the archived README.

- **Assessment:** A workflow for structured, phased software delivery; confirm the successor's current maturity before using it in an active project.

## BMAD Method

- **Project link:** [Official source](https://github.com/bmad-code-org/BMAD-METHOD)

- **Type:** Agile AI-driven development method with role-based agents and structured workflows.

- **Lifecycle:** Covers discovery, planning, architecture, implementation and iterative delivery.

- **Release maturity:** The README distinguishes stable v6.12 from v7 preview alpha; they have different maturity levels and installation paths.

- **Requirements:** The README lists Node.js 20.12+, Python 3.10+ and `uv` for setup.

- **Assessment:** Prefer the stable release line when reproducibility matters. Expect breaking changes and incomplete behavior when evaluating the v7 preview.

## MiroFish

- **Project link:** [Official source](https://github.com/666ghj/MiroFish)

- **Type:** Multi-agent swarm-intelligence simulation and scenario exploration platform.

- **Workflow:** Extracts seed information, builds a GraphRAG-backed environment, generates agents with personas/memory/behavior, runs simulations, and produces reports with interactive follow-up.

- **Stack requirements stated upstream:** Node.js 18+, Python 3.11–3.12 and `uv`; API credentials are required. The README demonstrates an LLM endpoint and Zep Cloud configuration.

- **Cost/limits:** Simulation can consume substantial model tokens; upstream advises starting with fewer than 40 rounds. External model and memory services may incur costs.

- **Assessment:** Useful for scenario exploration, narrative simulation and hypothesis generation. It is not a validated forecasting instrument. Simulated agent behavior is sensitive to seed data, prompts, model choice and configuration; do not treat outputs as reliable financial, political, policy or safety predictions without external validation.

## 📝 Note For Reader

Agent frameworks may execute shell commands, edit files, access networks, or delegate tasks. Review permission boundaries, tool policies, secrets handling, and sandbox support before connecting them to valuable repositories or accounts.
