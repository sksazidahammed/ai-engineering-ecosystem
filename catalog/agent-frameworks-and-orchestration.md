# Agent Frameworks and Orchestration

**Catalogue version:** 1.3  
**Last updated:** 2026-11-12 19:02 IST (UTC+05:30)

| Project | Provisional classification | Source | Status |
|---|---|---|---|
| gstack | Agent workflow / tool collection | [Submitted repository](https://github.com/garrytan/gstack) | Candidate — review pending |
| Caveman | Exact project unclear | [Discovery search](https://github.com/search?q=Caveman+Claude+Code&type=repositories) | Needs clarification |
| Claude-Mem | Agent memory / context system | [Submitted repository](https://github.com/thedotmack/claude-mem) | Candidate — review pending |
| Headroom | Context / token optimization project; exact identity unresolved | [Discovery search](https://github.com/search?q=Headroom+LLM+context&type=repositories) | Needs clarification |
| GSD | Agentic development workflow; intended project unresolved | [Submitted repository](https://github.com/open-gsd/gsd-core) | Candidate — review pending |
| BMAD Method | Agentic software-development framework | [Submitted repository](https://github.com/bmad-code-org/BMAD-METHOD) | Candidate — review pending |\n| MiroFish | Multi-agent swarm simulation / scenario exploration engine | [666ghj/MiroFish](https://github.com/666ghj/MiroFish) | Verified identity; predictive validity not established |

## MiroFish\n\n- **Repository:** [666ghj/MiroFish](https://github.com/666ghj/MiroFish)\n- **Type:** Multi-agent swarm-intelligence simulation and scenario exploration platform.\n- **Workflow:** Extracts seed information, builds a GraphRAG-backed environment, generates agents with personas/memory/behavior, runs simulations, and produces reports with interactive follow-up.\n- **Stack requirements stated upstream:** Node.js 18+, Python 3.11–3.12 and `uv`; API credentials are required. The README demonstrates an LLM endpoint and Zep Cloud configuration.\n- **Cost/limits:** Simulation can consume substantial model tokens; upstream advises starting with fewer than 40 rounds. External model and memory services may incur costs.\n- **Assessment:** Useful for scenario exploration, narrative simulation and hypothesis generation. It is not a validated forecasting instrument. Simulated agent behavior is sensitive to seed data, prompts, model choice and configuration; do not treat outputs as reliable financial, political, policy or safety predictions without external validation.\n\n## Classification guidance

This category covers multi-step agent execution, orchestration, persistent memory, role-based workflows, and project-level automation. It does not imply that every listed project is a general-purpose framework; individual records will be split into more precise subtypes after verification.

## Reader notes

Agent frameworks may execute shell commands, edit files, access networks, or delegate tasks. Review permission boundaries, tool policies, secrets handling, and sandbox support before connecting them to valuable repositories or accounts.
