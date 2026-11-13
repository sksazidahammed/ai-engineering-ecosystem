---
id: secure-vibe-coded-web-app          # kebab-case, matches file name
title: Ship a secure web app with an AI coding agent
audience: beginner                      # beginner | intermediate | advanced
outcome: A deployed web app with tests, security review and documentation.
last_reviewed: YYYY-MM-DD
records_used: []                        # catalogue record ids referenced below
---

# {{title}}

**Outcome:** what exists when you are done.
**Use this when:** one or two sentences on the situation.
**Not for:** when to pick a different playbook.

## Prerequisites
- Accounts, keys, runtimes (link catalogue records where relevant)

## Steps

### 1. Plan  *(lifecycle: plan)*
- **Do:** what to do, in one or two sentences.
- **Use:** `record-id` — why this one.
- **Alternatives:** `other-record-id`
- **Done when:** a checkable condition.

### 2. Design  *(lifecycle: design)*
(same shape)

### 3. Build  *(lifecycle: build)*
(same shape)

### 4. Test  *(lifecycle: test)*
(same shape)

### 5. Secure  *(lifecycle: secure)*
- Review the `risk` block of every record you installed before you run it.
- Run at least one code-security-review tool; record what it found.

### 6. Ship and operate  *(lifecycle: ship, operate)*
(same shape)

## Security checklist
- [ ] Every installed tool's risk level reviewed; high/critical ones sandboxed
- [ ] No long-lived credentials reachable by agents
- [ ] Hooks and install scripts read before running

## Common pitfalls
- Short, concrete, learned-the-hard-way items

## Related playbooks
- `other-playbook-id`
