# Agent Frameworks and Orchestration

**Catalogue version:** 1.6  
**Last updated:** 2026-11-12 19:50 IST (UTC+05:30)

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

A role-based coding-agent workflow that packages product, design, engineering management, code review, QA, security and release responsibilities as tools/skills. The README states MIT licensing and describes browser-driven QA and automated review flows. Setup requires a compatible coding agent and local dependencies; some features have additional platform/toolchain prerequisites. Treat security and release automation as review aids, not approval to merge unreviewed changes.

## Caveman

A coding-agent skill plus optional proxy/runtime that rewrites conversational output into shorter forms while aiming to preserve code correctness. The README documents benchmark results and an explicit split license: skill/adoption surfaces are MIT, while engine-linked runtime components are BSL-1.1 source-available with a future change date and commercial restrictions for third-party hosting. Read the component-level license before deploying or redistributing the runtime.

## Claude-Mem

A persistent memory system for coding agents. It records session activity, compresses observations and retrieves relevant context in later sessions; the README documents support across multiple agents. Requires a local worker/runtime and stores project/session context, so inspect data retention, database location, redaction and model/API configuration before using it with secrets or private repositories. Apache-2.0 stated upstream.

## Headroom

A context-compression layer for agent prompts, tool outputs, logs, RAG chunks and conversation history. Upstream describes local/in-process compression and reports token savings on selected workloads. Compression effectiveness varies by content; validate semantic fidelity on your own tasks, especially code, logs and structured data. Apache-2.0 stated upstream.

## GSD Core

The submitted `gsd-build/get-shit-done` repository is archived and explicitly points to `open-gsd/gsd-core` as the active successor. The directory therefore links to the successor, not the archived repository. Re-check the successor's current installation, release and license before adopting it; do not use old install instructions from the archived README.

## BMAD Method

An agile AI-driven development method covering discovery, planning, architecture, implementation and iterative delivery. The current README distinguishes stable v6.12 from v7 preview alpha, with different maturity and installation paths. It lists Node.js 20.12+, Python 3.10+ and `uv` for setup. Prefer the stable line when reproducibility matters; expect breaking changes on v7 preview.

## MiroFish

- **Repository:** [666ghj/MiroFish](https://github.com/666ghj/MiroFish)
- **Type:** Multi-agent swarm-intelligence simulation and scenario exploration platform.
- **Workflow:** Extracts seed information, builds a GraphRAG-backed environment, generates agents with personas/memory/behavior, runs simulations, and produces reports with interactive follow-up.
- **Stack requirements stated upstream:** Node.js 18+, Python 3.11–3.12 and `uv`; API credentials are required. The README demonstrates an LLM endpoint and Zep Cloud configuration.
- **Cost/limits:** Simulation can consume substantial model tokens; upstream advises starting with fewer than 40 rounds. External model and memory services may incur costs.
- **Assessment:** Useful for scenario exploration, narrative simulation and hypothesis generation. It is not a validated forecasting instrument. Simulated agent behavior is sensitive to seed data, prompts, model choice and configuration; do not treat outputs as reliable financial, political, policy or safety predictions without external validation.

## Classification guidance

This category covers multi-step agent execution, orchestration, persistent memory, role-based workflows, and project-level automation. It does not imply that every listed project is a general-purpose framework; individual records will be split into more precise subtypes after verification.

## Reader notes

Agent frameworks may execute shell commands, edit files, access networks, or delegate tasks. Review permission boundaries, tool policies, secrets handling, and sandbox support before connecting them to valuable repositories or accounts.
