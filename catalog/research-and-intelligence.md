# Research and Intelligence

**Catalogue version:** 1.0  
**Last updated:** 2026-11-12 17:39 IST (UTC+05:30)

| Project | Provisional classification | Source | Status |
|---|---|---|---|
| Graphify | Research / knowledge-graph project; exact identity unresolved | [Discovery search](https://github.com/search?q=Graphify&type=repositories) | Needs clarification |
| Agent Reach | CLI / agent web-research infrastructure | [Official repository](https://github.com/Panniantong/Agent-Reach) | Verified |
| Understand Anything | Research / understanding tool; exact identity unresolved | [Discovery search](https://github.com/search?q=Understand+Anything&type=repositories) | Needs clarification |
| Last 30 Days | Research skill / workflow | [Submitted repository](https://github.com/mvanhorn/last30days-skill) | Candidate — review pending |
| Career Ops | Career workflow / agent project | [Submitted repository](https://github.com/career-ops-hq/career-ops) | Candidate — review pending |
| REA | Acronym is ambiguous; exact project needs confirmation | [Submitted repository](https://github.com/morluto/rea) | Candidate — review pending |

## Verified entry: Agent Reach

- **Type:** CLI and agent-facing internet research infrastructure.
- **Purpose:** Provides an agent with search/read access to multiple online sources through a unified command-line workflow.
- **Source:** [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)
- **Installation guidance:** [Official installation documentation](https://github.com/Panniantong/Agent-Reach/blob/main/docs/install.md)
- **License:** MIT, as stated by the project.
- **Operational caveats:** Some sources require login or API credentials. Some integrations are described by the project as experimental. The project is primarily read-oriented; verify the current support matrix and requirements in its documentation before use.
- **Security note:** Browser-session reuse exposes the agent to the privileges of that session. Prefer a separate, low-privilege account and avoid sharing a primary personal browser profile.

## Reader notes

Research agents can ingest untrusted web content. Treat retrieved pages, posts, and documents as data rather than instructions. Verify important claims against primary sources, and review the data-access model before connecting personal accounts.
