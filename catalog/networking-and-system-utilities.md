# Networking and System Utilities

**Catalogue version:** 1.16
**Last updated:** 2026-11-13 18:24 IST (UTC+05:30)

| Project | Classification | Official repository | Status |
|---|---|---|---|
| net-merge | Multi-network connection aggregation utility | [net-merge/net-merge](https://github.com/net-merge/net-merge) | Repository identity verified; throughput claims untested |
| Plexo | Desktop download manager with multi-network acceleration | [anmolkapil/plexo](https://github.com/anmolkapil/plexo) | Repository identity verified; performance claims untested |
| Transfer | Android local-network file server for device-to-device transfer | [matan-h/Transfer](https://github.com/matan-h/Transfer) | Repository identity verified; LAN exposure requires care |
| abtop | Cross-platform terminal dashboard and Rust library for monitoring AI coding-agent sessions | [graykode/abtop](https://github.com/graykode/abtop) | MIT; JSON snapshots may contain sensitive local context |
| Herdr | Runtime and coordination layer for coding agents | [herdrdev/herdr](https://github.com/herdrdev/herdr) | Apache-2.0 stated upstream |
| Worktrunk | Git worktree management CLI for parallel development | [max-sixty/worktrunk](https://github.com/max-sixty/worktrunk) | MIT OR Apache-2.0 stated upstream |
| Gortex | Local code-intelligence engine with CLI, MCP server and graph UI | [zzet/gortex](https://github.com/zzet/gortex) | Apache-2.0 stated upstream |

## net-merge

- **Project link:** [Official source](https://github.com/net-merge/net-merge)

- **Type:** Multi-network connection aggregation utility.

- **Purpose:** The README describes combining Wi-Fi, Ethernet and phone hotspots so traffic can use multiple internet connections.

- **Platforms stated upstream:** Windows, macOS, Linux and Android.

- **Assessment:** Relevant to users with multiple independent connections. Actual throughput depends on the bonding/relay architecture, server path, latency, ISP behavior and application protocol. Do not assume ordinary local link aggregation automatically multiplies a single TCP connection's speed; inspect the technical design and test with your own routes.

## Plexo

- **Project link:** [Official source](https://github.com/anmolkapil/plexo)

- **Type:** Desktop download manager / multi-network download acceleration application.

- **Purpose:** The README describes combining Wi-Fi, Ethernet and mobile connections to accelerate file and torrent downloads.

- **Platforms stated upstream:** macOS, Windows and Linux.

- **Assessment:** Similar problem space to net-merge, but the README frames Plexo around download acceleration. Treat these as separate implementations; do not infer equivalent networking architecture or performance.

## Transfer

- **Project link:** [Official source](https://github.com/matan-h/Transfer)

- **Type:** Android local file-server application for transferring files between devices on the same Wi-Fi network.

- **Workflow:** The phone serves a selected folder over HTTP; other devices connect through a browser. The README describes upload/download, clipboard-to-text-file, command-line access and IP-based allow/deny prompts.

- **Security:** Password protection is optional and off by default. Use only on a trusted LAN, keep access prompts enabled, share a dedicated folder rather than broad storage, and stop the server when finished. HTTP traffic on an untrusted network can expose transferred data.

- **Assessment:** Useful for direct phone-to-PC transfers without cloud storage or cables; it is not an internet-hosted cloud drive.

## abtop

- **Project link:** [Official source](https://github.com/graykode/abtop)

- **Type:** Cross-platform terminal user interface (TUI), command-line utility and Rust library for monitoring local AI coding-agent sessions.

- **Purpose:** Provides a btop-style overview of Claude Code, Codex CLI and OpenCode sessions, including token usage, context-window percentage where supported, rate limits, Git state, child processes and listening ports.

- **Workflow:** Discovers sessions from local process and file state. It can display multiple profiles, identify orphaned ports, jump to supported terminal multiplexers, and emit one-shot JSON snapshots for scripts or other dashboards. The main monitoring view is read-only; explicit key actions can terminate a selected session or orphaned port.

- **Installation:** macOS/Linux installer, Windows PowerShell installer, prebuilt release binaries, or `cargo install abtop`. Rust/Cargo is needed only for source/package installation. OpenCode discovery requires the `sqlite3` CLI; Linux and Windows setup notes specify installing it separately.

- **Integrations:** Claude Code, Codex CLI and OpenCode. Terminal jump support includes cmux, tmux and iTerm2 on macOS. The Rust library API can be embedded by other local tools.

- **License / cost:** MIT. The project states that the TUI needs no API keys or authentication. Claude session summaries generated with `claude --print` make an indirect API call and may consume the user's Claude quota.

- **Privacy / security:** Reads local session files, process metadata and open-port information. The TUI does not display prompt text or file contents, but JSON snapshots can include bounded chat messages, tool previews, paths, commands and project context. Keep snapshots private and do not expose them through shared logs or network dashboards without access controls.

- **Limitations:** Feature coverage differs by agent; for example, OpenCode does not provide every context, task or rate-limit field. Terminal layout is best at 120×40 or larger. OpenCode monitoring depends on the local SQLite CLI. The README's platform and feature matrix is upstream documentation, not independent testing.

- **Assessment:** A focused local observability tool for developers running several coding agents concurrently. It monitors agent sessions rather than replacing or orchestrating them.

## Herdr

- **Project link:** [Official source](https://github.com/herdrdev/herdr)

- **Type / Classification:** Runtime and coordination layer for coding agents.

- **Purpose / Capabilities:** A developer tool described as the runtime where coding agents operate; official documentation provides a quick start and releases include a Homebrew formula.

- **Installation / Requirements:** Follow official quick-start and platform installation instructions; verify supported agent runtimes.

- **License / Cost:** Apache-2.0 stated upstream.

- **Privacy / Security / Limitations:** Review execution isolation, shell access and approval boundaries before connecting agents to valuable repositories or credentials.

## Worktrunk

- **Project link:** [Official source](https://github.com/max-sixty/worktrunk)

- **Type / Classification:** Git worktree management CLI for parallel development.

- **Purpose / Capabilities:** CLI for managing Git worktrees and parallel branches, useful when multiple developers or coding agents need isolated working directories.

- **Installation / Requirements:** Install through the documented package/release route; Git and a supported shell are required.

- **License / Cost:** MIT OR Apache-2.0, as stated upstream.

- **Privacy / Security / Limitations:** Worktrees isolate working directories, not credentials, network access or system privileges. Review repository hooks and scripts.

## Gortex

- **Project link:** [Official source](https://github.com/zzet/gortex)

- **Type / Classification:** Local code-intelligence engine with CLI, MCP server and graph UI.

- **Purpose / Capabilities:** Indexes repositories into a persistent knowledge graph of code entities and relationships, then exposes graph-grounded discovery, impact analysis and editing workflows through CLI, MCP and web UI. README describes multi-repository and multi-agent support.

- **Installation / Requirements:** Single-binary releases are listed for macOS, Linux and Windows; build-from-source requires Go and CGO/tree-sitter bindings. Agent setup and per-repository initialization are documented upstream.

- **License / Cost:** Apache-2.0, as stated by the official project site and repository.

- **Privacy / Security / Limitations:** The graph and resolver confidence are aids, not proof of correctness. Review file access, MCP tool exposure and edit-safety workflows; token-reduction and language-coverage claims are upstream-reported.

## 📝 Note For Reader

Network aggregation products can route traffic through relays or remote infrastructure. Review privacy, traffic encryption, relay ownership, routing behavior, bandwidth limits and whether all traffic or only supported downloads is affected. Benchmark with controlled tests before relying on advertised speed gains.
