# Agent Frameworks and Orchestration

**Catalogue version:** 1.15
**Last updated:** 2026-11-13 02:25 IST (UTC+05:30)

| Project | Provisional classification | Source | Status |
|---|---|---|---|
| gstack | Role-based engineering workflow and tool collection | [garrytan/gstack](https://github.com/garrytan/gstack) | Repository identity verified; MIT stated upstream |
| Caveman | Agent skill and proxy/runtime for token-efficient agent communication | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | Verified identity; split MIT/BSL-1.1 license |
| Claude-Mem | Persistent coding-agent memory and context system | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | Repository identity verified; inspect data retention and redaction |
| Headroom | Local context-compression middleware for prompts, tool outputs and agent history | [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | Verified identity; savings depend on workload and content |
| GSD Core | Spec-driven development and context-engineering workflow; successor to archived GSD repo | [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) | Successor identified; recheck current release and license |
| BMAD Method | Agile AI-driven development framework with role-based agents | [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | Repository identity verified; stable v6 and preview v7 differ in maturity |
| MiroFish | Multi-agent swarm simulation / scenario exploration engine | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | Verified identity; predictive validity not established |
| Foreman | Runtime for semantic supervision of coding-agent workers | [thruwire/foreman](https://github.com/thruwire/foreman) | MIT; requires a decision-model provider and worker runtime |
| Engram | Persistent memory service for AI coding agents | [Gentleman-Programming/engram](https://github.com/Gentleman-Programming/engram) | MIT stated upstream |
| GBrain | Source-attributed, user-controlled memory layer for agents | [garrytan/gbrain](https://github.com/garrytan/gbrain) | MIT stated upstream; hosted gbrain.io is optional paid service |
| OpenClaw | Self-hosted personal AI assistant and agent runtime | [openclaw/openclaw](https://github.com/openclaw/openclaw) | MIT stated upstream |
| Orkas | Local-first multi-agent desktop workspace | [Orkas-AI/Orkas](https://github.com/Orkas-AI/Orkas) | MIT stated upstream |
| OpenBot | Local-first desktop workspace for persistent AI teammates | [nightly-labs/openbot](https://github.com/nightly-labs/openbot) | PolyForm Noncommercial 1.0.0 stated upstream |
| Cindy | Open-source desktop AI agent for work on the user's computer | [makecindy/cindy](https://github.com/makecindy/cindy) | Apache-2.0 stated upstream |
| Macro | Unified team workspace combining communication, documents, tasks and agents | [macro-inc/macro](https://github.com/macro-inc/macro) | License not confirmed in this intake; hosted product |
| T3 Code | Open-source control plane for local coding agents | [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | License not confirmed in this intake |
| Harness² | Research framework for recursive agent harnessing and evaluation | [google-research/harness2](https://github.com/google-research/harness2) | Apache-2.0 stated upstream |
| LearnHarness | Agent harness for adaptive AI-assisted learning | [amosblomqvist/learnharness](https://github.com/amosblomqvist/learnharness) | License not confirmed in this intake |

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

## Foreman

- **Project link:** [Official source](https://github.com/thruwire/foreman)

- **Type:** Python `asyncio` runtime that supervises coding-agent workers through a separate semantic decision loop.

- **Workflow:** A worker such as Codex, OpenCode, Hermes or Deep Agents performs the coding task. Foreman independently evaluates bounded evidence—job requirements, worker activity, repository changes, test results and recent events—and can continue, steer, stop, retry, request verification or escalate to a human.

- **Architecture:** Worker backends and decision-model providers are replaceable. The README documents Jev and OpenAI Decisions API adapters; the decision layer evaluates typed predicates while Python policy and configured thresholds determine interventions.

- **Installation / requirements:** The project is a Python CLI/runtime; the README documents package installation and worker-specific setup. Some backends require separately installed coding-agent CLIs and provider credentials. Check the current worker guide for exact extras and supported versions.

- **License / cost:** MIT. Decision-model API calls and the selected worker's model usage may incur separate provider charges or quotas.

- **Limitations:** Probabilities and thresholds require calibration for the chosen model and workflow. A high completion probability is not proof that code is correct; independent tests and human review remain necessary. Live steering is backend-dependent.

- **Assessment:** Interesting supervisory layer for agent-driven software tasks, especially when a separate verifier and explicit completion criteria are needed. Start with a disposable repository and conservative intervention permissions.

## Engram

- **Project link:** [Official source](https://github.com/Gentleman-Programming/engram)

- **Type / Classification:** Persistent memory service for AI coding agents.

- **Purpose / Capabilities:** Provides persistent memory across coding-agent sessions, with local or cloud deployment options and integrations for multiple agents. It is a memory component rather than a general-purpose autonomous agent.

- **Installation / Requirements:** Follow upstream setup for the chosen storage/deployment mode and supported agent adapters.

- **License / Cost:** MIT, as stated by the repository.

- **Privacy / Security / Limitations:** Memory can retain sensitive code, prompts and project decisions. Review storage location, synchronization, access control, deletion and cloud data flow.

## GBrain

- **Project link:** [Official source](https://github.com/garrytan/gbrain)

- **Type / Classification:** Source-attributed, user-controlled memory layer for agents.

- **Purpose / Capabilities:** Stores explicit facts with sources and supports correction and withdrawal. It offers keyword retrieval first, with optional semantic search, synthesis and enrichment; multiple agents can share a brain.

- **Installation / Requirements:** Self-host/local install instructions are in the README; optional managed hosting is available separately.

- **License / Cost:** MIT for the repository; hosted service may have separate pricing and terms.

- **Privacy / Security / Limitations:** Review sharing permissions and the content root exposed to agents. Memory improves continuity but can preserve stale or incorrect facts until corrected.

## OpenClaw

- **Project link:** [Official source](https://github.com/openclaw/openclaw)

- **Type / Classification:** Self-hosted personal AI assistant and agent runtime.

- **Purpose / Capabilities:** Runs an assistant on the user's own devices and connects it to chat interfaces, tools and configured model providers. It is a full agent runtime, not merely a prompt collection.

- **Installation / Requirements:** Requires Node.js and configured model/channel credentials; follow the current official install and security guidance.

- **License / Cost:** MIT, as stated upstream; model and messaging providers may charge separately.

- **Privacy / Security / Limitations:** Broad integrations and device access create a significant attack surface. Use least-privilege accounts, isolate the runtime, protect tokens and review every exposed tool/channel.

## Orkas

- **Project link:** [Official source](https://github.com/Orkas-AI/Orkas)

- **Type / Classification:** Local-first multi-agent desktop workspace.

- **Purpose / Capabilities:** Coordinates a Commander and specialist agents around persistent projects, files, memory, to-dos and scheduled workflows; README lists integrations with several coding-agent runtimes.

- **Installation / Requirements:** Desktop downloads are provided for macOS and Windows; model/provider setup and supported agent CLIs are documented upstream.

- **License / Cost:** MIT, as stated upstream; model-provider subscriptions or API usage may cost extra.

- **Privacy / Security / Limitations:** Local-first storage does not make agents harmless: inspect shell/file permissions, auto-advance behavior and connected agent privileges. Keep human approval for consequential actions.

## OpenBot

- **Project link:** [Official source](https://github.com/nightly-labs/openbot)

- **Type / Classification:** Local-first desktop workspace for persistent AI teammates.

- **Purpose / Capabilities:** Provides separate agent workspaces and conversations, local queues, file transfer, embedded browser and agent-to-agent messaging across several coding agents.

- **Installation / Requirements:** Install a desktop release and configure supported agent CLIs/ACP integrations as described upstream.

- **License / Cost:** PolyForm Noncommercial 1.0.0; not a general-purpose commercial-use open-source license. Read the full terms.

- **Privacy / Security / Limitations:** README warns that agents can run with broad filesystem access. Treat agent workspaces as privileged execution environments and review command approval, isolation and data access.

## Cindy

- **Project link:** [Official source](https://github.com/makecindy/cindy)

- **Type / Classification:** Open-source desktop AI agent for work on the user's computer.

- **Purpose / Capabilities:** An out-of-the-box computer-use agent intended to connect a user's computers and phone and work with model subscriptions/providers the user already has.

- **Installation / Requirements:** Download from the official project website; follow current platform and model setup instructions.

- **License / Cost:** Apache-2.0 stated upstream; model/provider costs and terms are separate.

- **Privacy / Security / Limitations:** Computer-use agents can interact with files and applications. Review permissions, action confirmations, local network exposure and provider data policies before use.

## Macro

- **Project link:** [Official source](https://github.com/macro-inc/macro)

- **Type / Classification:** Unified team workspace combining communication, documents, tasks and agents.

- **Purpose / Capabilities:** The repository describes a workspace unifying email, messages, documents, tasks, calls, agents, CRM and databases with shared team-level memory and linked/searchable context.

- **Installation / Requirements:** The README directs users to the hosted Macro product and documentation; account and service availability may apply.

- **License / Cost:** Repository license and hosted pricing require direct confirmation; do not assume the hosted product is free or self-hostable.

- **Privacy / Security / Limitations:** Centralizing email, CRM and team memory concentrates sensitive business data. Review retention, access controls, connectors, export and vendor terms.

## T3 Code

- **Project link:** [Official source](https://github.com/pingdotgg/t3code)

- **Type / Classification:** Open-source control plane for local coding agents.

- **Purpose / Capabilities:** Runs coding agents on a local machine through a unified interface, with remote continuation and approval from mobile or web clients; README lists several coding-agent integrations.

- **Installation / Requirements:** Install the desktop app and configure supported local agent CLIs; mobile and web clients are documented upstream.

- **License / Cost:** License not confirmed in this intake; model/provider subscriptions remain separate.

- **Privacy / Security / Limitations:** Remote approvals and control surfaces should be protected with account security and network controls. Review which commands require approval and where session data is stored.

## Harness²

- **Project link:** [Official source](https://github.com/google-research/harness2)

- **Type / Classification:** Research framework for recursive agent harnessing and evaluation.

- **Purpose / Capabilities:** Research code and benchmark workflows for studying systems that recursively improve or configure agent harnesses. README defines a harness as prompts, tools, memory, skills and orchestration around a model.

- **Installation / Requirements:** Python environment; README documents editable installation and JobBench setup. Rendering extras and benchmark dependencies may be required.

- **License / Cost:** Apache-2.0 stated upstream; benchmark model/API usage may incur costs.

- **Privacy / Security / Limitations:** Research benchmark results depend on tasks, models and evaluation setup. Treat reported scores as experimental, not proof of general agent capability.

## LearnHarness

- **Project link:** [Official source](https://github.com/amosblomqvist/learnharness)

- **Type / Classification:** Agent harness for adaptive AI-assisted learning.

- **Purpose / Capabilities:** Plans lessons from a learner's current understanding toward a target, adapts instruction from answers and reasoning, and carries a persistent knowledge graph across sessions.

- **Installation / Requirements:** A downloadable application and documentation are linked from the project README; confirm supported platforms and model setup upstream.

- **License / Cost:** License and model-provider pricing were not confirmed in this intake.

- **Privacy / Security / Limitations:** Learning profiles and answers can be sensitive personal data. Check storage, export/deletion, model-provider routing and whether educational claims have been independently evaluated.

## 📝 Note For Reader

Agent frameworks may execute shell commands, edit files, access networks, or delegate tasks. Review permission boundaries, tool policies, secrets handling, and sandbox support before connecting them to valuable repositories or accounts.
