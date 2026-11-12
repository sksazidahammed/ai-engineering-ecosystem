# Verification Policy

**Policy version:** 1.0  
**Last updated:** 2026-11-12 17:39 IST (UTC+05:30)

## 1. Source hierarchy

1. Official upstream repository maintained by the project owner.
2. Official documentation or release page linked from that repository.
3. Official package registry entry linked by the project.
4. Maintainer announcements and issue discussions.
5. Independent technical reviews, used as supplementary evidence only.

Search pages, mirrors, forks, social posts, and third-party lists are discovery sources, not proof of canonical identity.

## 2. Status definitions

- **Verified:** Canonical identity and basic project type are established from an official source.
- **Candidate — review pending:** A plausible source was supplied, but identity, current state, or project details have not been sufficiently checked.
- **Needs clarification:** The name is ambiguous, the exact repository is unknown, or the supplied link is only a search query.
- **Archived / inactive:** Upstream evidence indicates the project is archived or no longer maintained. Record the evidence and date.
- **Removed:** The project is no longer included, with reason recorded in the changelog.

## 3. What verification covers

For each project, aim to establish:

- Canonical repository and owner.
- Project purpose and accurate category.
- Actual artifact type: skill, plugin, MCP server, CLI, app, library, framework, or service.
- Supported agents, platforms, and runtime requirements.
- Installation method and external dependencies.
- License and any usage restrictions.
- Maintenance signals: recent commits, releases, issue activity, and archived status.
- Permission model, network access, credential handling, and other security implications.
- Pricing or API requirements, where applicable.

## 4. Evidence and uncertainty

Do not infer features from a project name. Do not convert maintainer claims into independently tested facts. Label uncertain details and link to the source that supports each material claim. If sources conflict, state the conflict rather than silently selecting one.

## 5. Safety review

Inspect installation scripts and dependency sources before recommending execution. Flag broad filesystem, shell, browser-session, network, or credential access. Recommend least privilege and sandboxing for agent tools that execute code or process untrusted input.

## 6. Update discipline

Every published catalogue update must include a version, date, and time in India Standard Time (IST, UTC+05:30). Update the changelog, preserve prior records unless there is a documented reason to remove them, merge duplicates, and recheck affected internal links.
