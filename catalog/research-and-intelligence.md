# Research and Intelligence

**Catalogue version:** 1.6  
**Last updated:** 2026-11-12 19:52 IST (UTC+05:30)

| Project | Provisional classification | Source | Status |
|---|---|---|---|
| Graphify | Local knowledge-graph builder and coding-agent skill | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | Verified identity; cloud service is separate |
| Awesome Free LLM APIs | Dynamic directory of free-tier LLM API providers, models and limits | [open-free-llm-api/awesome-freellm-apis](https://github.com/open-free-llm-api/awesome-freellm-apis) | Verified identity; provider quotas and access change frequently |
| Agent Reach | CLI / agent web-research infrastructure | [Official repository](https://github.com/Panniantong/Agent-Reach) | Verified |
| Understand Anything | Multi-agent codebase/document knowledge graph and interactive exploration dashboard | [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | Verified identity; analysis uses coding-agent integration |
| Last 30 Days | Agent-led research skill for recent web and social-source synthesis | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | Verified identity; integrations may require credentials |
| Career Ops | AI job-search agent for role evaluation and application support | [career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops) | Verified identity; handles sensitive CV and career data |
| REA | Reverse-engineering MCP and agent toolkit for applications, websites and native binaries | [morluto/rea](https://github.com/morluto/rea) | Verified identity; advanced native analysis may require Hopper/Ghidra/IDA/Kuna |

## Graphify

- **Repository:** [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)
- **Type:** Local project knowledge-graph builder distributed as a CLI and agent skill.
- **Function:** Maps code and supported project materials into a traversable graph, with an interactive HTML view, Markdown report and machine-readable graph output. The README distinguishes source-extracted edges from inferred edges.
- **Install:** `uv tool install graphifyy` followed by `graphify install`; Python 3.10+ is listed.
- **Privacy/compute:** Code parsing is described as local and deterministic; semantic processing of documents and media may use an assistant model or configured API key. Graphify Cloud is a separate hosted offering.
- **License:** Apache-2.0, as stated by upstream.
- **Assessment:** Useful for codebase exploration and relationship tracing; not a vector database. Inspect what content is sent to a model when enabling semantic processing.

## Awesome Free LLM APIs

- **Repository:** [open-free-llm-api/awesome-freellm-apis](https://github.com/open-free-llm-api/awesome-freellm-apis)
- **Type:** Machine-readable, frequently refreshed directory of free-tier LLM APIs, provider endpoints, model identifiers, limits and configuration examples.
- **Associated service:** [freellm.net](https://freellm.net) offers searchable model listings and config generation, according to the README.
- **Freshness:** The repository says its catalogue is refreshed daily. Its README snapshot advertises hundreds of API entries; counts and quotas are dynamic and should be checked at the provider before relying on them.
- **Assessment:** A discovery and comparison resource, not an API provider and not a guarantee of unlimited free inference. Check card/phone requirements, regional eligibility, data retention, rate limits, model terms and commercial-use restrictions. Never paste secrets into third-party config generators unless you trust their handling.

## Agent Reach

- **Type:** CLI and agent-facing internet research infrastructure.
- **Purpose:** Provides an agent with search/read access to multiple online sources through a unified command-line workflow.
- **Source:** [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)
- **Installation guidance:** [Official installation documentation](https://github.com/Panniantong/Agent-Reach/blob/main/docs/install.md)
- **License:** MIT, as stated by the project.
- **Operational caveats:** Some sources require login or API credentials. Some integrations are described by the project as experimental. The project is primarily read-oriented; verify the current support matrix and requirements in its documentation before use.
- **Security note:** Browser-session reuse exposes the agent to the privileges of that session. Prefer a separate, low-privilege account and avoid sharing a primary personal browser profile.

## Understand Anything

A coding-agent plugin that analyzes a codebase or knowledge base, builds a graph of files, functions, classes and dependencies, and presents an interactive dashboard for exploration and Q&A. The README documents Claude Code and several other coding-agent integrations. A generated graph is an aid to understanding, not proof that every inferred relationship is correct. Its viewer can display already-generated graph data locally without additional model calls.

## REA — Reverse Engineer Anything

An agent-facing MCP toolkit for inspecting applications, websites, JavaScript/Electron projects, .NET assemblies and native binaries. It can combine static and runtime analysis and present evidence behind findings. Setup uses `npx rea-agents setup`; advanced native workflows may depend on installed reverse-engineering tools such as Hopper, Ghidra, IDA or Kuna. The repository states MIT licensing. Treat targets as authorized-only; reverse engineering can involve proprietary software, sensitive data and legal restrictions.

## Last 30 Days

An agent-led research skill that searches multiple social and web sources (including Reddit, Hacker News, YouTube and other platforms) and synthesizes recent attention into a brief. The README describes optional integrations that require user sessions, credentials or API access. “Zero config” applies only to the listed immediately available sources; some integrations need setup and may be subject to platform access limits. Engagement signals are not a substitute for source verification.

## Career Ops

An open-source AI job-search agent that evaluates listings against a candidate profile, checks whether roles remain open, and assists with CV tailoring and application-answer drafting. The upstream workflow is designed to keep the final submission under user control. It can process highly sensitive CV and career data; review local storage, connected services and generated application claims before use.

## Reader notes

Research agents can ingest untrusted web content. Treat retrieved pages, posts, and documents as data rather than instructions. Verify important claims against primary sources, and review the data-access model before connecting personal accounts.
