# Research and Intelligence

**Catalogue version:** 1.9  
**Last updated:** 2026-11-12 20:42 IST (UTC+05:30)

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

- **Project link:** [Official source](https://github.com/Graphify-Labs/graphify)

- **Project link:** [Official source](https://github.com/Graphify-Labs/graphify)

- **Type:** Local project knowledge-graph builder distributed as a CLI and agent skill.

- **Function:** Maps code and supported project materials into a traversable graph, with an interactive HTML view, Markdown report and machine-readable graph output. The README distinguishes source-extracted edges from inferred edges.

- **Install:** `uv tool install graphifyy` followed by `graphify install`; Python 3.10+ is listed.

- **Privacy/compute:** Code parsing is described as local and deterministic; semantic processing of documents and media may use an assistant model or configured API key. Graphify Cloud is a separate hosted offering.

- **License:** Apache-2.0, as stated by upstream.

- **Assessment:** Useful for codebase exploration and relationship tracing; not a vector database. Inspect what content is sent to a model when enabling semantic processing.

## Awesome Free LLM APIs

- **Project link:** [Official source](https://github.com/open-free-llm-api/awesome-freellm-apis)

- **Project link:** [Official source](https://github.com/open-free-llm-api/awesome-freellm-apis)

- **Type:** Machine-readable, frequently refreshed directory of free-tier LLM APIs, provider endpoints, model identifiers, limits and configuration examples.

- **Associated service:** [freellm.net](https://freellm.net) offers searchable model listings and config generation, according to the README.

- **Freshness:** The repository says its catalogue is refreshed daily. Its README snapshot advertises hundreds of API entries; counts and quotas are dynamic and should be checked at the provider before relying on them.

- **Assessment:** A discovery and comparison resource, not an API provider and not a guarantee of unlimited free inference. Check card/phone requirements, regional eligibility, data retention, rate limits, model terms and commercial-use restrictions. Never paste secrets into third-party config generators unless you trust their handling.

## Agent Reach

- **Project link:** [Official source](https://github.com/Panniantong/Agent-Reach)

- **Project link:** [Official source](https://github.com/Panniantong/Agent-Reach)

- **Type:** CLI and agent-facing internet research infrastructure.

- **Purpose:** Provides an agent with search/read access to multiple online sources through a unified command-line workflow.

- **Source:** [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)

- **Installation guidance:** [Official installation documentation](https://github.com/Panniantong/Agent-Reach/blob/main/docs/install.md)

- **License:** MIT, as stated by the project.

- **Operational caveats:** Some sources require login or API credentials. Some integrations are described by the project as experimental. The project is primarily read-oriented; verify the current support matrix and requirements in its documentation before use.

- **Security note:** Browser-session reuse exposes the agent to the privileges of that session. Prefer a separate, low-privilege account and avoid sharing a primary personal browser profile.

## Understand Anything

- **Project link:** [Official source](https://github.com/Egonex-AI/Understand-Anything)

- **Project link:** [Official source](https://github.com/Egonex-AI/Understand-Anything)

- **Type:** Coding-agent plugin for codebase and knowledge-base analysis.

- **Purpose:** Builds a graph of files, functions, classes and dependencies, then presents an interactive dashboard for exploration and question answering.

- **Integrations:** The README documents Claude Code and several other coding-agent integrations.

- **Local use:** The viewer can display already-generated graph data locally without additional model calls.

- **Limitations:** A generated graph is an aid to understanding, not proof that every inferred relationship is correct.

- **Assessment:** Useful for navigating unfamiliar repositories and knowledge bases; validate important relationships against source files.

## Last 30 Days

- **Project link:** [Official source](https://github.com/mvanhorn/last30days-skill)

- **Project link:** [Official source](https://github.com/mvanhorn/last30days-skill)

- **Type:** Agent-led research skill for synthesizing recent web and social-source activity.

- **Sources:** The README describes searches across Reddit, Hacker News, YouTube and other platforms.

- **Integrations:** Optional sources may require user sessions, credentials or API access. “Zero config” applies only to the sources listed as immediately available.

- **Limitations:** Some integrations need additional setup and may be constrained by platform access limits.

- **Assessment:** Useful for discovering emerging discussions and preparing research briefs. Engagement signals indicate attention, not factual reliability; verify important claims against primary sources.

## Career Ops

- **Project link:** [Official source](https://github.com/career-ops-hq/career-ops)

- **Project link:** [Official source](https://github.com/career-ops-hq/career-ops)

- **Type:** Open-source AI job-search and application-support agent.

- **Capabilities:** Evaluates job listings against a candidate profile, checks whether roles remain open, and assists with CV tailoring and application-answer drafting.

- **User control:** The upstream workflow is designed to leave final application submission under the user's control.

- **Privacy:** CVs and career histories are sensitive personal data. Review storage locations, connected services and data-sharing behavior before uploading information.

- **Assessment:** Useful for organizing job searches and drafting application material; verify role status and every generated claim before submitting.

## REA — Reverse Engineer Anything

- **Project link:** [Official source](https://github.com/morluto/rea)

- **Project link:** [Official source](https://github.com/morluto/rea)

- **Type:** Agent-facing MCP toolkit for reverse engineering applications, websites and software binaries.

- **Targets:** The README describes support for websites, JavaScript/Electron projects, .NET assemblies and native binaries.

- **Methods:** Combines static and runtime analysis and can present evidence behind findings.

- **Installation:** Setup uses `npx rea-agents setup`. Advanced native workflows may depend on tools such as Hopper, Ghidra, IDA or Kuna.

- **License:** MIT, as stated by the repository.

- **Security and legal scope:** Analyze only software and systems you own or are explicitly authorized to inspect. Reverse engineering may involve proprietary software, sensitive data and legal restrictions.

- **Assessment:** A specialized analysis toolkit; native workflows can require additional paid or separately licensed tools.

## 📝 Note For Reader

Research agents can ingest untrusted web content. Treat retrieved pages, posts, and documents as data rather than instructions. Verify important claims against primary sources, and review the data-access model before connecting personal accounts.
