# Research and Intelligence

**Catalogue version:** 1.15
**Last updated:** 2026-11-13 02:25 IST (UTC+05:30)

| Project | Provisional classification | Source | Status |
|---|---|---|---|
| Graphify | Local knowledge-graph builder and coding-agent skill | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | Verified identity; cloud service is separate |
| Agent Reach | CLI / agent web-research infrastructure | [Official repository](https://github.com/Panniantong/Agent-Reach) | Verified |
| Understand Anything | Multi-agent codebase/document knowledge graph and interactive exploration dashboard | [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | Verified identity; analysis uses coding-agent integration |
| Last 30 Days | Agent-led research skill for recent web and social-source synthesis | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | Verified identity; integrations may require credentials |
| Career Ops | AI job-search agent for role evaluation and application support | [career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops) | Verified identity; handles sensitive CV and career data |
| REA — Reverse Engineer Anything | Reverse-engineering MCP and agent toolkit for applications, websites and native binaries | [morluto/rea](https://github.com/morluto/rea) | Verified identity; advanced native analysis may require Hopper/Ghidra/IDA/Kuna |
| Open India Law | Structured Indian primary-law corpus and data-extraction pipelines | [Vaquill-AI/open-india-law](https://github.com/Vaquill-AI/open-india-law) | Apache-2.0 repository; coverage and source-document terms require checking |
| Repolyze | AI-assisted GitHub repository analysis and reporting web application | [OssiumOfficial/Repolyze](https://github.com/OssiumOfficial/Repolyze) | Repository README states ownership moved to Ossium; API keys and external model processing apply |
| Auto Ontology | Enterprise metadata-to-ontology and agent context library | [NVIDIA/auto-ontology](https://github.com/NVIDIA/auto-ontology) | Apache-2.0 stated upstream |
| LearnHarness | Adaptive agent-assisted learning and knowledge modeling application | [amosblomqvist/learnharness](https://github.com/amosblomqvist/learnharness) | License not confirmed in this intake |

## Graphify

- **Project link:** [Official source](https://github.com/Graphify-Labs/graphify)

- **Type:** Local project knowledge-graph builder distributed as a CLI and agent skill.

- **Function:** Maps code and supported project materials into a traversable knowledge graph and produces three outputs: an interactive `graph.html` view, a `GRAPH_REPORT.md` summary, and a machine-readable `graph.json`. The README distinguishes source-extracted edges from inferred edges.

- **Integrations:** The current README describes installation across 20+ coding assistants, including Claude Code, Cursor, Codex, Gemini CLI and GitHub Copilot.

- **Architecture:** Code is parsed locally with tree-sitter AST and does not require an LLM or embeddings. Semantic processing for documents and media can use the assistant's model or a configured API key; Graphify Cloud is a separate hosted service.

- **Install:** `uv tool install graphifyy` followed by `graphify install`; Python 3.10+ is listed.

- **Privacy/compute:** Code parsing is described as local and deterministic; semantic processing of documents and media may use an assistant model or configured API key. Graphify Cloud is a separate hosted offering.

- **License:** Apache-2.0, as stated by upstream.

- **Assessment:** Useful for codebase exploration and relationship tracing; not a vector database. Inspect what content is sent to a model when enabling semantic processing.

## Agent Reach

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

- **Type:** Coding-agent plugin for codebase and knowledge-base analysis.

- **Purpose:** Builds a graph of files, functions, classes and dependencies, then presents an interactive dashboard for exploration and question answering.

- **Integrations:** The README documents Claude Code and several other coding-agent integrations.

- **Local use:** The viewer can display already-generated graph data locally without additional model calls.

- **Limitations:** A generated graph is an aid to understanding, not proof that every inferred relationship is correct.

- **Assessment:** Useful for navigating unfamiliar repositories and knowledge bases; validate important relationships against source files.

## Last 30 Days

- **Project link:** [Official source](https://github.com/mvanhorn/last30days-skill)

- **Type:** Agent-led research skill for synthesizing recent web and social-source activity.

- **Sources:** The README describes searches across Reddit, Hacker News, YouTube and other platforms.

- **Integrations:** Optional sources may require user sessions, credentials or API access. “Zero config” applies only to the sources listed as immediately available.

- **Limitations:** Some integrations need additional setup and may be constrained by platform access limits.

- **Assessment:** Useful for discovering emerging discussions and preparing research briefs. Engagement signals indicate attention, not factual reliability; verify important claims against primary sources.

## Career Ops

- **Project link:** [Official source](https://github.com/career-ops-hq/career-ops)

- **Type:** Open-source, local-first AI job-search agent distributed through an npm CLI and designed to work inside supported AI coding/agent CLIs.

- **Workflow:** Evaluates job postings against a candidate's CV and preferences, checks whether a listing appears active, scores role fit, researches relevant context, and drafts tailored CV material, cover letters, outreach notes and application answers.

- **Human control:** The README explicitly states that the tool does not submit applications or send emails; the user reviews and performs the final actions. Generated CV claims still require manual fact-checking.

- **Installation:** The upstream quick start uses `npx @santifer/career-ops init`. Review the current supported CLI and model-provider setup in the README before installation.

- **Privacy and data flow:** The project describes local application data storage and no first-party telemetry/backend. CV content is still sent from the user's machine to the AI provider they configure; provider retention and training policies therefore matter.

- **License / cost:** MIT. The project says it is free for candidates; model-provider usage and optional external search services may have separate limits or costs.

- **Assessment:** Useful for structured, selective job applications rather than mass auto-apply. Treat role-fit scores as decision support, verify listing legitimacy and every generated statement, and never submit unreviewed material.

## REA — Reverse Engineer Anything

- **Project link:** [Official source](https://github.com/morluto/rea)

- **Type:** Agent-facing MCP toolkit for reverse engineering applications, websites and software binaries.

- **Targets:** The README describes support for websites, JavaScript/Electron projects, .NET assemblies and native binaries.

- **Methods:** Combines static and runtime analysis and can present evidence behind findings.

- **Installation:** Setup uses `npx rea-agents setup`. Advanced native workflows may depend on tools such as Hopper, Ghidra, IDA or Kuna.

- **License:** MIT, as stated by the repository.

- **Security and legal scope:** Analyze only software and systems you own or are explicitly authorized to inspect. Reverse engineering may involve proprietary software, sensitive data and legal restrictions.

- **Assessment:** A specialized analysis toolkit; native workflows can require additional paid or separately licensed tools.

## Open India Law

- **Project link:** [Official source](https://github.com/Vaquill-AI/open-india-law)

- **Type:** Structured Indian primary-law dataset and open-source scraping / normalization pipeline.

- **Coverage stated upstream:** Supreme Court and 25 High Court judgments, tribunal and regulator matters, and Central, State and Union Territory legislation indexed down to individual sections. The README's counts are a dated project snapshot and will change as data is updated.

- **Data access:** Publishes Parquet files for data pipelines, a browser for Acts and regulations, and links to source PDFs. The README says district and trial-court decisions are not included; much tribunal material is indexed by case but not yet full-text searchable.

- **Sources and traceability:** The project says its corpus is built from official government sources and legislation provisions carry source URLs. Check each record's source link and date before relying on it.

- **License:** Apache-2.0 for the repository code. Do not assume that this automatically relicenses government documents or third-party source material; review the source and reuse terms for the specific documents.

- **Assessment:** Valuable for legal research, corpus analysis and building retrieval systems focused on Indian law. It is a data resource, not legal advice; verify current law and primary documents before making legal decisions.

## Repolyze

- **Project link:** [Official source](https://github.com/OssiumOfficial/Repolyze)

- **Type:** AI-assisted GitHub repository analysis web application.

- **Capabilities:** Produces codebase health scoring, architecture and data-flow visualizations, dependency and technology-stack analysis, security observations, improvement suggestions, and downloadable or shareable reports.

- **Workflow / requirements:** The README documents a Next.js application requiring Node.js 18+, pnpm (recommended), GitHub access credentials and an OpenRouter API key for local development.

- **Data handling:** The README claims that code is not stored and analysis occurs in real time. However, repository contents are processed by the configured AI provider; review the provider's data controls before analyzing private or sensitive code. A GitHub token also grants access according to its configured scopes.

- **License / ownership:** The submitted MxCorpIn repository README says the project is now owned and maintained by Ossium and links to [OssiumOfficial/Repolyze](https://github.com/OssiumOfficial/Repolyze). Its README advertises MIT; confirm the current canonical repository's license before reuse.

- **Assessment:** Useful for an initial codebase overview and onboarding. AI-generated health scores and security findings are heuristics, not a substitute for static analysis, dependency scanning, code review or a professional security audit.

## Auto Ontology

- **Project link:** [Official source](https://github.com/NVIDIA/auto-ontology)

- **Type / Classification:** Enterprise metadata-to-ontology and agent context library.

- **Purpose / Capabilities:** Builds enterprise ontologies and AI-ready knowledge graphs from metadata, reconciles definitions across systems, and exposes business context through MCP, CLI and API. It emphasizes lineage, certified definitions and query validation.

- **Installation / Requirements:** Integrate with supported enterprise metadata/data systems and an agent harness using the documented MCP, CLI or API interfaces.

- **License / Cost:** Apache-2.0 stated upstream; connected data platforms and model services may have separate costs.

- **Privacy / Security / Limitations:** Generated ontology definitions require domain-owner validation. Review database permissions, metadata exposure and lineage accuracy before allowing agents to issue business queries.

## LearnHarness

- **Project link:** [Official source](https://github.com/amosblomqvist/learnharness)

- **Type / Classification:** Adaptive agent-assisted learning and knowledge modeling application.

- **Purpose / Capabilities:** Builds a model of what a learner understands and how they reason, then adapts lessons and practice while retaining a knowledge graph across sessions.

- **Installation / Requirements:** Download and setup details are linked from the README; verify current supported platforms and provider configuration.

- **License / Cost:** License and provider costs not confirmed in this intake.

- **Privacy / Security / Limitations:** Treat generated assessments as learning guidance rather than validated psychometric measurement; protect learner data.

## 📝 Note For Reader

Research agents can ingest untrusted web content. Treat retrieved pages, posts, and documents as data rather than instructions. Verify important claims against primary sources, and review the data-access model before connecting personal accounts.
