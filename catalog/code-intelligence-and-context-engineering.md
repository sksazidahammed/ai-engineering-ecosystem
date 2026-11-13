# Code Intelligence and Context Engineering

**Catalogue version:** 1.16  
**Last updated:** 2026-11-13 18:24 IST (UTC+05:30)

| Project | Classification | Official source | Status |
|---|---|---|---|
| Serena | Semantic code retrieval and editing MCP server | [oraios/serena](https://github.com/oraios/serena) | GPL-3.0-or-later stated in README |
| CodeGraph | Local semantic code intelligence engine | [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | MIT stated in README |
| code-review-graph | Local code knowledge graph for review | [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | MIT stated in README |
| GitNexus | Codebase knowledge graph and explorer | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | PolyForm Noncommercial 1.0.0 stated in README |
| jCodeMunch MCP | AST-based symbol retrieval MCP server | [jgravelle/jcodemunch-mcp](https://github.com/jgravelle/jcodemunch-mcp) | README reports benchmark token savings |
| Repomix | Codebase-to-context packer | [yamadashy/repomix](https://github.com/yamadashy/repomix) | Review ignore rules before sharing output |
| Context Mode | Local context-compression plugin | [mksglu/context-mode](https://github.com/mksglu/context-mode) | ELv2 stated in README |
| LeanCTX | Context gateway and policy layer | [yvgude/lean-ctx](https://github.com/yvgude/lean-ctx) | Mixed license stated in README |
| AgentMemory | Cross-agent persistent memory | [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) | Review storage, synchronization, encryption and retention behavior before storing secrets or personal data. |
| ai-memory | Cross-agent long-term workstream memory | [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | MIT stated in README |
| RTK | Coding-agent token and command-output optimizer | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | License is split between Apache-2.0 and BUSL-1.1 |
| Mindwalk | Local coding-agent session visualizer | [cosmtrek/mindwalk](https://github.com/cosmtrek/mindwalk) | Optional session evaluation sends a session summary to the model behind the user's CLI |

## Serena

- **Project link:** [Official source](https://github.com/oraios/serena)

- **Type / Classification:** Semantic code retrieval and editing MCP server.

- **Purpose:** Exposes symbol-level code retrieval, editing, refactoring and debugging tools to coding agents through MCP.

- **Workflow / Requirements:** README describes a Python-based MCP integration and a newer REPL-based interface; consult current setup docs.

- **License / Cost / Status:** GPL-3.0-or-later stated in README; inspect tool permissions before granting repository write access.

## CodeGraph

- **Project link:** [Official source](https://github.com/colbymchenry/codegraph)

- **Type / Classification:** Local semantic code intelligence engine.

- **Purpose:** Builds code graphs to provide coding agents with structured, repository-aware context across supported agents.

- **Workflow / Requirements:** README describes a Rust-powered, local-first tool with an npm distribution and bundled runtime.

- **License / Cost / Status:** MIT stated in README; index contents may reveal proprietary source structure.

## code-review-graph

- **Project link:** [Official source](https://github.com/tirth8205/code-review-graph)

- **Type / Classification:** Local code knowledge graph for review.

- **Purpose:** Builds a local code knowledge graph and exposes precise review context to AI coding tools through MCP.

- **Workflow / Requirements:** README lists Python 3.10+, PyPI distribution and MCP compatibility.

- **License / Cost / Status:** MIT stated in README; review findings require human validation.

## GitNexus

- **Project link:** [Official source](https://github.com/abhigyanpatwari/GitNexus)

- **Type / Classification:** Codebase knowledge graph and explorer.

- **Purpose:** Indexes symbols, calls, dependencies and execution flows into a knowledge graph accessible through CLI, MCP and a web graph explorer.

- **Workflow / Requirements:** README specifies Node.js 22.18+ or 24.11+ and commands to analyze a repository and configure editors.

- **License / Cost / Status:** PolyForm Noncommercial 1.0.0 stated in README; commercial use is restricted.

## jCodeMunch MCP

- **Project link:** [Official source](https://github.com/jgravelle/jcodemunch-mcp)

- **Type / Classification:** AST-based symbol retrieval MCP server.

- **Purpose:** Uses tree-sitter parsing to retrieve source by symbol rather than requiring agents to read whole files.

- **Workflow / Requirements:** README lists multiple MCP-compatible coding clients and publishes a reproducible benchmark methodology.

- **License / Cost / Status:** README reports benchmark token savings; those figures are upstream claims. License badge says dual-use; inspect LICENSE for permitted uses.

## Repomix

- **Project link:** [Official source](https://github.com/yamadashy/repomix)

- **Type / Classification:** Codebase-to-context packer.

- **Purpose:** Packages repository contents into AI-friendly formats so coding agents can analyze a codebase with fewer manual file operations.

- **Workflow / Requirements:** Available as a CLI and online service; exact output and filtering options are documented upstream.

- **License / Cost / Status:** Review ignore rules before sharing output; packed files can contain secrets or proprietary code.

## Context Mode

- **Project link:** [Official source](https://github.com/mksglu/context-mode)

- **Type / Classification:** Local context-compression plugin.

- **Purpose:** Keeps tool output and related context processing outside the coding agent's main context window; the local plugin is distinct from its hosted Gateway service.

- **Workflow / Requirements:** README describes integrations for multiple coding agents and local processing.

- **License / Cost / Status:** ELv2 stated in README; hosted Gateway has separate account/subscription terms.

## LeanCTX

- **Project link:** [Official source](https://github.com/yvgude/lean-ctx)

- **Type / Classification:** Context gateway and policy layer.

- **Purpose:** Sits between AI tools and information sources to select relevant context and apply supported access/content controls before delivery.

- **Workflow / Requirements:** README describes local CLI, MCP, hooks and proxy paths, plus an SDK.

- **License / Cost / Status:** Mixed license stated in README; inspect component terms and validate policy coverage before relying on it as a security boundary.

## AgentMemory

- **Project link:** [Official source](https://github.com/rohitg00/agentmemory)

- **Type / Classification:** Cross-agent persistent memory.

- **Purpose:** Stores and retrieves memory across coding sessions and multiple agent clients, including MCP-compatible clients.

- **Workflow / Requirements:** README describes persistent memory integrations across several coding-agent hosts.

- **License / Cost / Status:** Review storage, synchronization, encryption and retention behavior before storing secrets or personal data.

## ai-memory

- **Project link:** [Official source](https://github.com/akitaonrails/ai-memory)

- **Type / Classification:** Cross-agent long-term workstream memory.

- **Purpose:** Shares project context and handoffs between coding agents so work can continue across tools and sessions.

- **Workflow / Requirements:** README describes a Rust CLI and a shared workstream/handoff protocol; Rust 1.95+ is stated.

- **License / Cost / Status:** MIT stated in README; verify local data paths and any synchronization or external-provider behavior.

## RTK

- **Project link:** [Official source](https://github.com/rtk-ai/rtk)

- **Type / Classification:** Coding-agent token and command-output optimizer.

- **Purpose:** A Rust-based cost-reduction layer that transforms common developer command outputs for more efficient agent context use.

- **Workflow / Requirements:** README advertises Homebrew distribution and pipeline support.

- **License / Cost / Status:** License is split between Apache-2.0 and BUSL-1.1; inspect edition/component terms. Savings depend on workload.

## Mindwalk

- **Project link:** [Official source](https://github.com/cosmtrek/mindwalk)

- **Type / Classification:** Local coding-agent session visualizer.

- **Purpose:** Replays coding-agent sessions on a 3D map of a codebase to show where an agent explored, read and edited.

- **Workflow / Requirements:** README describes a Go binary that reads Claude Code, Codex and pi session logs; visualization is local.

- **License / Cost / Status:** Optional session evaluation sends a session summary to the model behind the user's CLI; local viewing and evaluation have different data flows.

## 📝 Note For Reader

Entries are categorized by their primary use. A repository README review verifies the submitted identity and upstream-described scope; it does not constitute hands-on installation, performance, security or legal testing. Recheck current upstream documentation, license files and provider terms before deployment.
