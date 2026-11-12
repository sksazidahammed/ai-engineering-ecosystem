# Editorial and Maintenance Rulebook

**Rulebook version:** 1.0  
**Directory baseline:** 1.12  
**Last updated:** 2026-11-12 21:35 IST (UTC+05:30)  
**Applies to:** Every category page, the master catalogue, README, changelog, and all future submissions.

This document is the authoritative operating standard for maintaining the AI Engineering Ecosystem Directory. Follow it before researching, editing, adding, moving, correcting, or removing any catalogue record. If a future request conflicts with a rule here, preserve the established standard and ask for clarification before making a conflicting structural change.

## 1. Non-negotiable editorial structure

### 1.1 Category-page order

Every category page must follow this sequence:

1. Category title.
2. Catalogue version and last-updated timestamp.
3. Summary table.
4. Individual project explanation sections, in exactly the same order as the table.
5. One final reader-note section titled exactly **📝 Note For Reader**.

Do not insert unrelated commentary between these parts. Do not add multiple closing-note sections.

### 1.2 Summary table and explanation parity

- Every project row in the summary table must have exactly one corresponding detailed explanation section.
- Every detailed project explanation must have a corresponding summary-table row.
- The order of project rows and explanation headings must match exactly.
- Preserve the established order unless the user explicitly requests reordering or a documented editorial correction requires it.
- Do not rank by stars, popularity, downloads, or social attention unless the user explicitly approves a clear ranking method.
- Do not add or remove records during a formatting-only cleanup.

### 1.3 Project links

Every individual project explanation must begin immediately after its heading with exactly one consistently formatted link field:

`- **Project link:** [Official source](https://...)`

- Use the canonical upstream repository for GitHub projects.
- Use the official website or primary documentation for hosted products and non-GitHub projects.
- Use an official successor link when a submitted repository is archived and a successor is clearly identified; preserve the historical repository context where relevant.
- Never guess, fabricate, or silently substitute a URL.
- Do not use search-result pages, unofficial mirrors, or unrelated forks as official links.
- Keep additional documentation links inside the relevant labelled field, such as Installation or Documentation.
- Do not repeat the same Project link elsewhere in the same explanation unless there is a clear reader benefit.
- The summary table may retain its own repository/source column. That does not replace the required Project link in the detailed explanation.

### 1.4 Detailed explanation format

Use concise, labelled, point-by-point bullets. Put a blank line between bullets.

Possible fields include:

- **Type / Classification**
- **Purpose**
- **Capabilities**
- **Workflow / Architecture**
- **Installation**
- **Requirements**
- **Technology / Integrations**
- **Model support**
- **License**
- **Cost**
- **Privacy / Security**
- **Limitations**
- **Assessment / Best use**

Use only fields that are relevant and supported by evidence. Do not force every project into every field. Do not collapse a project explanation into a plain paragraph when the surrounding catalogue uses structured bullets.

The Project link is always the first bullet. The remaining bullets follow a logical order: what it is, what it does, how it works, setup and dependencies, license/cost, risks/limitations, and practical assessment.

### 1.5 No stray metadata or unlabelled text

This is a strict rule.

- Do not place status badges, verification summaries, classification strings, license snippets, or metadata lines between the Project link and the labelled explanation bullets.
- Do not use standalone HTML such as `<small>...`, inline status ribbons, or decorative metadata in project sections.
- Every factual detail belongs under a clear field label.
- Put repository identity status in the summary table or an appropriate labelled field only when it helps readers.
- Put license details under **License**, not in a free-floating status line.
- Put project type under **Type / Classification**, not in an unlabelled string.
- Distinguish identity verification from functional, security, and performance testing.
- Avoid repeating the same fact in both a status line and a detailed bullet.

### 1.6 One closing section only

Every category page must end with exactly:

`## 📝 Note For Reader`

This is the only permitted category-page closing-note heading. Do not use alternatives such as:

- Reader notes
- Editorial notes
- Classification guidance
- Additional notes
- General remarks

The note must be brief, direct, and useful. Include only essential caveats that apply to the category as a whole, such as authorization, privacy, changing quotas, licensing, or the need to recheck upstream instructions. Do not repeat project-level caveats already explained. Do not put editorial process commentary or internal maintenance instructions here.

## 2. Research and source verification

### 2.1 Source hierarchy

Use sources in this order:

1. Canonical upstream repository maintained by the project owner.
2. Official documentation, releases, and issue/announcement pages linked by upstream.
3. Official package registry or distribution page linked by upstream.
4. Maintainer statements and discussions.
5. Independent technical reviews as supplementary evidence.

Search results, mirrors, forks, social posts, and third-party directories are discovery aids, not proof of canonical identity.

### 2.2 Identify the actual artifact

Classify what the project actually is. Examples include:

- Agent skill / instruction pack
- Plugin / extension
- MCP server
- CLI
- Desktop or web application
- Library / SDK
- Framework / orchestration system
- API gateway / hosted service
- Dataset / model / model adapter
- Curated collection / learning resource

Do not call every repository an application, plugin, framework, or AI agent. A collection is not a single installable product. A skill is not automatically a standalone scanner or service.

### 2.3 Research each submission

Inspect the official README and relevant official documentation. Establish, where available:

- Canonical name, owner, URL, and repository identity.
- Actual purpose and supported workflows.
- Installation steps and runtime prerequisites.
- Supported platforms, coding agents, APIs, and integrations.
- Dependencies, external services, credentials, and permissions.
- License and any component-level or model/data licensing distinctions.
- Pricing, API usage, hosted-service dependencies, and free-tier limits.
- Privacy, telemetry, data processing, storage, and credential handling.
- Maintenance signals, releases, archived status, and known limitations.

If a detail cannot be verified, label it unknown or omit it. Never fill gaps with assumptions.

### 2.4 Attribute claims accurately

- Distinguish **repository identity verified** from hands-on functional testing.
- Attribute benchmark, speed, accuracy, security, and performance claims to upstream unless independently reproduced.
- Never claim hands-on testing when only README or documentation research was performed.
- Do not call software safe, secure, production-ready, actively maintained, or reliable without sufficient evidence.
- Record the date for volatile facts such as provider quotas, model availability, pricing, and maintenance status.

### 2.5 License and cost discipline

- Distinguish the repository's code license from licenses for models, weights, adapters, datasets, assets, dependencies, and hosted services.
- Record split or changing licenses at the component level.
- Do not infer commercial-use rights from a permissive license on only part of a project.
- A free API tier is not unlimited or guaranteed. Note relevant quotas, region/account restrictions, rate limits, provider terms, and possible paid usage.
- Do not describe a product as free if essential hosted services or API calls may cost money.

### 2.6 Security and privacy

Review execution privileges, shell access, filesystem access, browser/session access, network exposure, credential handling, telemetry, and data retention when relevant.

Flag dual-use security tools and autonomous execution risks. Recommend authorization, least privilege, sandboxing, isolation, and operator review where appropriate. Never imply that a sandbox removes the need for authorization.

## 3. Record management

- Preserve existing records and useful history.
- Check for duplicates before adding a project. Merge duplicate submissions into one canonical record while preserving useful alternate names or context.
- Do not remove a record without a documented reason in the changelog.
- If a repository changes owner, is archived, or has a successor, preserve that history and link the current official destination when verified.
- Create a new category only when it improves navigation and the category has a meaningful scope.
- Keep category placement based on the project's primary function, not merely its marketing description.
- A formatting-only change must not silently alter project facts, descriptions, links, or membership.

## 4. Writing and cognitive-load standards

- Write for a technically curious reader who may be new to the project.
- Prefer concrete, direct explanations over promotional language.
- Keep bullets short and focused; split compound ideas when that improves comprehension.
- Avoid redundant caveats, filler, decorative emojis, status badges, and repeated metadata.
- Use consistent field names and consistent spacing across all category pages.
- Use an emoji only where the established design explicitly calls for it: the closing heading **📝 Note For Reader**.
- Do not introduce a new heading or formatting convention in one category without considering its effect across the entire directory.

## 5. Required update workflow

For every batch of new submissions or maintenance request:

1. Read this rulebook and the relevant verification/evaluation policies.
2. Fetch the current live GitHub files before editing; never rely only on remembered or previously generated content.
3. Research every submitted project from its official source.
4. Identify duplicates and determine the correct category.
5. Plan all affected files and preserve existing records.
6. Edit the category page, master catalogue, README/navigation, and changelog as applicable.
7. Update version and timestamp metadata consistently. Use India Standard Time (IST, UTC+05:30).
8. Keep table rows and detailed explanation sections in identical order.
9. Apply the exact Project link placement and the single **📝 Note For Reader** closing section.
10. Fetch the published files after each write and verify the actual committed content.

## 6. Mandatory pre-publication audit

Do not declare an update complete until the following checks pass for every affected category page:

- [ ] Every summary-table row has one matching explanation heading.
- [ ] Every explanation heading has one matching summary-table row.
- [ ] Table order and explanation order are identical.
- [ ] Every project explanation begins with exactly one **Project link** bullet.
- [ ] The project link resolves to a verified official or primary source.
- [ ] No unlabelled text, HTML metadata, status ribbon, or verification string appears between the Project link and structured bullets.
- [ ] Explanation fields are labelled, concise, and separated by a blank line.
- [ ] No paragraph-only project explanation has slipped into the structured format.
- [ ] Exactly one **📝 Note For Reader** section exists, and it is the final section.
- [ ] The reader note is concise, practical, and non-repetitive.
- [ ] No alternate closing headings remain.
- [ ] No unintended project additions, removals, or duplicates occurred.
- [ ] Links, licenses, requirements, and material caveats remain intact.
- [ ] Version and timestamp metadata are correct and consistent.
- [ ] README, master catalogue, and changelog reflect the update where applicable.
- [ ] The final live GitHub content has been fetched and checked.

For a formatting-only audit, report counts and detected exceptions. Automated pattern checks are useful but do not prove semantic accuracy; manually inspect suspicious sections and representative entries. Never report zero issues unless the audit actually checked for them.

## 7. GitHub execution and reporting

- Use the connected GitHub tools to modify the repository when the user asks for an actual update.
- Fetch the current file and use its latest SHA before updating it.
- After writing, fetch the file again to verify the exact published content.
- Never claim a commit or update succeeded without a successful tool response and post-write verification.
- Report the version, files changed, what changed, verification performed, and any unresolved limitations.
- Clearly distinguish completed edits from recommendations or work not performed.
- Keep explanations of GitHub operations simple and transparent.

## 8. Conflict resolution and change control

The user's explicit current request can authorize a deliberate change to this rulebook. Otherwise, treat this document as the default standard.

If a request appears to conflict with an established rule, do not silently choose one interpretation. Explain the conflict briefly and ask one focused clarification before making a structural change.

When this rulebook changes, update its version and date, record the change in the changelog, and check whether README or category metadata needs updating.

---

## Quick reference

**Every project:** heading → one Project link bullet → concise labelled bullets with blank lines.

**Every category page:** title and metadata → table → explanations in table order → one final **📝 Note For Reader**.

**Every repository update:** fetch first → research → edit → fetch again → audit → report only verified results.
