# Cybersecurity and Security Auditing

**Catalogue version:** 1.8  
**Last updated:** 2026-11-12 20:20 IST (UTC+05:30)

| Project | Classification | Official repository | Status |
|---|---|---|---|
| Cloudflare Security Audit Skill | Coding-agent workflow for repository security auditing | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | Repository identity verified; not a standalone scanner |
| PentAGI | Self-hosted multi-agent penetration-testing platform | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | Repository identity verified; authorized testing only |

## Cloudflare Security Audit Skill

<small>Verified identity · Coding-agent skill · MIT license (per upstream project)</small>


- **Official repository:** [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)

- **Classification:** Repository-level security auditing skill for coding agents. It is not a standalone vulnerability scanner.

- **Purpose:** Structures a security review into reconnaissance, coverage-led hunting, candidate validation, structured findings, independent verification, and reporting.

- **Outputs described by the project:** Architecture and coverage artifacts, machine-readable findings, and human-readable security reports.

- **Finding discipline:** Distinguishes confirmed findings, items needing validation, and rejected candidates. A suspected issue should not be presented as confirmed without evidence of the relevant boundary failure and impact.

- **Installation:** Follow the [official README](https://github.com/cloudflare/security-audit-skill/blob/main/README.md). The documented installation command is:
  
  `npx skills add https://github.com/cloudflare/security-audit-skill --skill security-audit`


- **Operational requirements:** The workflow expects a capable coding agent. The project emphasizes sandboxing and restricted execution for untrusted target code; follow its current safety guidance.

- **Limitations:** It is an audit workflow, not a replacement for professional penetration testing, secure development lifecycle controls, or independent review.

## PentAGI


- **Official repository:** [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi)

- **Type:** Self-hosted multi-agent penetration-testing system.

- **Purpose:** Coordinates specialized AI agents and 20+ security tools (the README names tools such as Nmap, Metasploit and sqlmap) inside Docker-based execution environments, then produces reports.

- **Model support:** The README describes multiple hosted providers and local model routes including Ollama and vLLM.

- **Deployment:** Docker/Compose or Podman guidance; the README lists minimum requirements of 2 vCPU, 4 GB RAM and 20 GB disk.

- **License:** MIT for the core project, according to the upstream README. VXControl Cloud services may require a separate license key and terms.

- **Risk classification:** High-impact dual-use security tooling. Sandbox claims do not remove the need for authorization, network isolation, scope limits, and operator oversight. Run only against systems you own or are explicitly authorized to test. Never point autonomous exploitation workflows at public or third-party targets without written authorization.

- **Assessment:** A specialized red-team / pentest automation platform, not a general coding assistant. Infrastructure and model costs may apply.

## Reader notes

Security tools can cause damage if granted broad access or run against systems without authorization. Audit only repositories and systems you own or are explicitly authorized to assess. Use isolated environments, least privilege, and controlled network access. Recheck upstream instructions before every installation because commands and requirements can change.
