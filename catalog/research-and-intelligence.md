# Research and Intelligence

**Catalogue version:** 1.3  
**Last updated:** 2026-11-12 19:02 IST (UTC+05:30)

| Project | Provisional classification | Source | Status |
|---|---|---|---|
| Graphify | Local knowledge-graph builder and coding-agent skill | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | Verified identity; cloud service is separate |
| Agent Reach | CLI / agent web-research infrastructure | [Official repository](https://github.com/Panniantong/Agent-Reach) | Verified |
| Understand Anything | Research / understanding tool; exact identity unresolved | [Discovery search](https://github.com/search?q=Understand+Anything&type=repositories) | Needs clarification |
| Last 30 Days | Research skill / workflow | [Submitted repository](https://github.com/mvanhorn/last30days-skill) | Candidate — review pending |
| Career Ops | Career workflow / agent project | [Submitted repository](https://github.com/career-ops-hq/career-ops) | Candidate — review pending |
| REA | Acronym is ambiguous; exact project needs confirmation | [Submitted repository](https://github.com/morluto/rea) | Candidate — review pending |

## Graphify\n\n- **Repository:** [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)\n- **Type:** Local project knowledge-graph builder distributed as a CLI and agent skill.\n- **Function:** Maps code and supported project materials into a traversable graph, with an interactive HTML view, Markdown report and machine-readable graph output. The README distinguishes source-extracted edges from inferred edges.\n- **Install:** `uv tool install graphifyy` followed by `graphify install`; Python 3.10+ is listed.\n- **Privacy/compute:** Code parsing is described as local and deterministic; semantic processing of documents and media may use an assistant model or configured API key. Graphify Cloud is a separate hosted offering.\n- **License:** Apache-2.0, as stated by upstream.\n- **Assessment:** Useful for codebase exploration and relationship tracing; not a vector database. Inspect what content is sent to a model when enabling semantic processing.\n\n## Awesome Free LLM APIs\n\n- **Repository:** [open-free-llm-api/awesome-freellm-apis](https://github.com/open-free-llm-api/awesome-freellm-apis)\n- **Type:** Machine-readable, frequently refreshed directory of free-tier LLM APIs, provider endpoints, model identifiers, limits and configuration examples.\n- **Associated service:** [freellm.net](https://freellm.net) offers searchable model listings and config generation, according to the README.\n- **Freshness:** The repository says its catalogue is refreshed daily. Its README snapshot advertises hundreds of API entries; counts and quotas are dynamic and should be checked at the provider before relying on them.\n- **Assessment:** A discovery and comparison resource, not an API provider and not a guarantee of unlimited free inference. Check card/phone requirements, regional eligibility, data retention, rate limits, model terms and commercial-use restrictions. Never paste secrets into third-party config generators unless you trust their handling.\n\n## Verified entry: Agent Reach

- **Type:** CLI and agent-facing internet research infrastructure.
- **Purpose:** Provides an agent with search/read access to multiple online sources through a unified command-line workflow.
- **Source:** [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)
- **Installation guidance:** [Official installation documentation](https://github.com/Panniantong/Agent-Reach/blob/main/docs/install.md)
- **License:** MIT, as stated by the project.
- **Operational caveats:** Some sources require login or API credentials. Some integrations are described by the project as experimental. The project is primarily read-oriented; verify the current support matrix and requirements in its documentation before use.
- **Security note:** Browser-session reuse exposes the agent to the privileges of that session. Prefer a separate, low-privilege account and avoid sharing a primary personal browser profile.

## Reader notes

Research agents can ingest untrusted web content. Treat retrieved pages, posts, and documents as data rather than instructions. Verify important claims against primary sources, and review the data-access model before connecting personal accounts.
