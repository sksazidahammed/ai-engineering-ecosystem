# Changelog

All notable directory changes are recorded here. Dates and times use India Standard Time (IST, UTC+05:30).

## Version 1.0 — 2026-11-12 17:39 IST

### Added
- Established the public directory homepage and navigation.
- Added the master catalogue and category pages for coding, research, agent frameworks, cybersecurity, design, writing/content, and productivity.
- Added verification policy and evaluation criteria.
- Added contribution guidelines.
- Consolidated the initial user-submitted collection into 29 distinct named records after merging the duplicate Anthropic skills submission.
- Added verified baseline records for Agent Reach and Cloudflare Security Audit Skill, with operational limitations and safety notes.

### Notes
- The remaining candidate records are explicitly marked as review pending or needing clarification.
- GitHub search URLs are discovery links, not canonical project links.
- No project has been declared safe or production-ready solely because it appears in this directory.


## Version 1.1 — 2026-11-12 17:45 IST

### Added / updated
- Added the submitted [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) repository to Coding and Development.
- Reclassified the earlier ambiguous “Karpathy Skills” candidate as a Claude Code plugin / agent instruction pack with Cursor project-rule support.
- Documented its four principles: think before coding, simplicity first, surgical changes, and goal-driven execution.
- Added a provenance caution: the repository's README points Claude Code marketplace and raw `CLAUDE.md` installation examples to `forrestchang/andrej-karpathy-skills`, so users should confirm the intended canonical source before installing.
- Recorded the upstream-stated MIT license and clarified that guidelines do not replace tests or code review.


## Version 1.2 — 2026-11-12 18:29 IST (UTC+05:30)

### Added
- Added 13 submitted repositories and classified them across four new and existing categories.
- Added PentAGI to cybersecurity; documented its self-hosted multi-agent penetration-testing workflow, infrastructure requirements, MIT core license statement, cloud-service distinction, and strict authorized-use warning.
- Added OpenReply and OpnForm to productivity and workflows, including self-hosting, Meta API, MCP, and AGPL licensing notes.
- Added Harper to writing and content, with its English-only scope and local grammar-checking focus.
- Created catalogues for media/audio/video, local AI and agent applications, networking/system utilities, and AI project collections.
- Added Cap, WhisperX, ManimGX, Henge, Jan, OpenMausBot, net-merge, Plexo, and Awesome LLM Apps.
- Recorded Henge's distinction between MIT application code and separately licensed model weights/adapters.
- Recorded that repository identity verification is not equivalent to hands-on performance, security, or feature testing.

### Editorial notes
- Project entries are categorized by actual function, not simply grouped as “AI tools.”
- Resource collections are distinguished from installable applications and frameworks.
- Dual-use security automation is explicitly flagged for authorized testing only.


## Version 1.3 — 2026-11-12 19:02 IST (UTC+05:30)

### Added / updated
- Added Addy Osmani Agent Skills to Coding and Development, including its engineering lifecycle commands, multi-agent installation routes and single-skill shared-reference portability caveat.
- Resolved the earlier Ponytail candidate to the submitted dietrichgebert/ponytail repository and classified it as a coding-agent workflow; benchmark claims remain attributed to upstream.
- Resolved Graphify to Graphify-Labs/graphify and documented its local knowledge-graph workflow, extracted/inferred edge distinction, CLI installation and cloud/local processing distinction.
- Added OmniRoute as a self-hosted multi-provider LLM API gateway. Its provider counts and free-tier estimates are treated as volatile third-party claims, not guaranteed quotas.
- Added MiroFish as a multi-agent swarm simulation platform and documented API/cost dependencies and the absence of demonstrated predictive validity.
- Added Awesome Free LLM APIs as a dynamic discovery directory, not an API provider; free-tier eligibility and quota data require direct provider verification.
- Created a Model Infrastructure and Gateways category.
- Updated catalogue version, navigation and timestamps.

### Reader notes
- Repository README claims, benchmark figures, provider counts and quota estimates are attributed to upstream and are not independently performance-tested.
- A free API tier may impose regional, identity, phone, card, rate-limit, data-use or commercial restrictions. Verify current terms with each provider before use.


## Version 1.4 — 2026-11-12 19:26 IST (UTC+05:30)

### Reconciliation and corrections
- Reconciled the user's recovered repository list against the existing catalogue. Most links were already represented as provisional records, so they were corrected and upgraded rather than duplicated.
- Added Transfer as a new distinct record under Networking and System Utilities.
- Resolved REA, Understand Anything, Headroom and Caveman to their actual repository identities and functions.
- Corrected repository owners/links for Taste Skill, PPT Master, Humanizer and HyperFrames; replaced the Diagram Design placeholder with its submitted repository.
- Marked the original gsd-build/get-shit-done repository as archived and linked the active successor, open-gsd/gsd-core.
- Added project-level summaries and material caveats for Superpowers, Matt Pocock Skills, ECC, BMAD Method, Claude-Mem, gstack, Career Ops, Last 30 Days, marketing/writing skills, design tools and video tools.
- Repaired malformed literal \
 sequences that had broken Markdown tables and navigation in affected catalogue files.
- Added a unique-record count note to the master catalogue. Counts refer to distinct catalogue records, not raw submission links or historical version additions.

### Reader notes
- Repository README and license statements are attributed to upstream; this update does not constitute hands-on security, performance or functional testing.
- GSD's submitted repository is archived; use the successor link and re-check its current release and license.
- Caveman has split licensing (MIT skill/adoption components and BSL-1.1 runtime components); review the component-level license.
- Transfer exposes a local HTTP file server; restrict access to trusted LAN devices and stop the server when not in use.


## Version 1.5 — 2026-11-12 19:44 IST (UTC+05:30)

### Catalogue structure and consistency
- Standardized category-page navigation so every category begins with a scannable project table before detailed project explanations.
- Added summary tables to Local AI and Agent Applications, Cybersecurity and Security Auditing, Productivity and Workflows, Media/Audio/Video, Networking and System Utilities, AI Project Collections, and Model Infrastructure and Gateways.
- Reconciled the Agent Frameworks and Orchestration index with its detailed entries, replacing stale candidate labels and placeholder repository links.
- Repaired escaped newline artifacts in category content and removed a duplicated Reader notes heading where present.
- Updated directory and catalogue metadata to version 1.5. No projects were added or removed; the distinct-record count is unchanged.

### Reader notes
- Tables are navigation summaries; detailed sections remain the source for setup, licensing, operational limitations and security caveats.
- Repository identity and README review do not imply hands-on testing or production validation.


## Version 1.6 — 2026-11-12 19:52 IST (UTC+05:30)

### Individual project documentation standard
- Removed the catch-all “Additional verified projects” and “Verified entry” groupings from category pages.
- Gave every affected project its own named section: Superpowers, Matt Pocock Skills, Everything Claude Code, Agent Reach, Understand Anything, REA, Last 30 Days, Career Ops, gstack, Claude-Mem, Headroom, Caveman, GSD Core, BMAD Method, Impeccable, Taste Skill and Archify.
- Replaced compressed bullet summaries in Design and Frontend with individual project sections.
- Added dedicated OpenMontage and HyperFrames explanations to Writing and Content, and added Harper to that category's index table to match its existing explanation.
- Updated affected category metadata, README and master-catalogue version to 1.6. The 48-record master catalogue count is unchanged.

### Editorial standard
- Every project listed in a category table must have its own named explanatory section in that category file.
- Each entry should describe project identity/type, purpose and workflow, installation or requirements where known, license and cost considerations where known, and material limitations/security/privacy caveats.
- Unknown or untested details must be explicitly marked as unknown or upstream-stated; they must not be guessed.
- Do not use catch-all headings such as “Additional verified projects” to group records.


### Version 1.6 consistency pass
- Added a dedicated Anthropic Agent Skills entry and a missing Awesome Free LLM APIs row to Research and Intelligence.
- Rebuilt Design and Frontend so all six indexed projects have their own full named sections; removed the duplicated Impeccable heading and compressed bullet list.
- Added Harper to the Writing and Content index, matching its existing individual explanation.
- Standardized all 12 category pages to version 1.6 and the same update timestamp.


## Version 1.7 — 2026-11-12 (IST)

### Fixed
- Reordered detailed project explanation sections in Coding and Development, Research and Intelligence, Agent Frameworks and Orchestration, and Writing and Content to match each page's summary-table sequence exactly.
- Audited all 12 category pages and confirmed that each listed project has a corresponding individual explanation section in the same order as its table.
- Preserved existing project descriptions, caveats, links, and classifications; this release is an ordering and consistency correction, not a popularity ranking or a new project intake.

### Editorial rule
- Category tables and detailed project sections must remain in identical project order. Popularity-based ranking is not applied because stars, online attention, and practical usefulness are distinct signals and no single ranking method has been adopted.


## Version 1.8 — 2026-11-12 20:20 IST (UTC+05:30)

### Fixed
- Standardized project explanation formatting across all 12 category pages.
- Converted previously paragraph-only project descriptions into clearly labeled, point-by-point fields where the source content supported it.
- Added consistent blank-line spacing between detail points so each item is visually distinct and easy to scan.
- Preserved the existing table order, project records, source links and substantive caveats.

### Editorial standard
- Each project entry should use a consistent, readable heading and a concise point-by-point explanation. Use only relevant fields (such as type, purpose, workflow, installation, requirements, license/cost, privacy/security, limitations and assessment); omit fields that are not applicable or not verified.
- Put a blank line between every bullet point. Avoid one-paragraph project descriptions and avoid inventing missing technical details.


## Version 1.9 — 2026-11-12 20:42 IST (UTC+05:30)

### Fixed
- Standardized the final section of every category page to the single heading **📝 Note For Reader**; removed alternate closing headings such as “Reader notes”, “Editorial notes” and “Classification guidance”.
- Shortened closing notes to concise, reader-facing caveats and removed generic editorial/classification commentary from category-page endings.
- Added a consistently placed **Project link** field immediately below every individual project heading, using the official repository or primary project source.
- Replaced inconsistent “Repository” and “Official repository” field labels with the single “Project link” label while retaining useful installation and documentation links.
- Preserved project records, descriptions, caveats, table order and explanation order.

### Editorial rule
- Every project explanation must begin with a **Project link** field pointing to its official repository or primary source.
- Every category page must end with exactly one **📝 Note For Reader** section. Keep it brief and limited to essential reader-facing cautions or clarifications.


## Version 1.10 — 2026-11-12 20:54 IST (UTC+05:30)

### Fixed
- Removed a stray inline metadata line from the Cloudflare Security Audit Skill explanation. Its classification remains in the Classification field and the upstream-stated MIT license is now in a dedicated License field.
- Audited all 12 category pages for the same formatting defect: unlabelled metadata or prose appearing between the Project link and the structured explanation bullets. No other instances were found.
- No project records, order, or substantive caveats changed.


## Version 1.11 — 2026-11-12 21:07 IST (UTC+05:30)

### Added
- Added [Editorial and Maintenance Rulebook](standards/EDITORIAL-AND-MAINTENANCE-RULEBOOK.md) as the authoritative operating standard for all future directory research, submissions, formatting, GitHub updates and verification.
- Consolidated the established editorial rules: table/explanation order parity, one official Project link at the start of every explanation, labelled point-by-point content, no stray metadata, and exactly one final **📝 Note For Reader** section.
- Added a mandatory pre-publication checklist covering project counts, order, links, formatting, reader notes, preservation, metadata, and post-write verification.
- Clarified evidence attribution, license/cost distinctions, security/privacy review, duplicate handling, and change-control expectations.

### Maintenance
- Linked the rulebook from the README so future contributors can find the standards before making changes.
- No project records were added, removed, or reclassified in this standards-only release.
