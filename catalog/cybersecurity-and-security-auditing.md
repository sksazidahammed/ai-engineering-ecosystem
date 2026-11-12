# Cybersecurity and Security Auditing

**Catalogue version:** 1.2  
**Last updated:** 2026-11-12 18:29 IST (UTC+05:30)

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

## PentAGI\n\n- **Official repository:** [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi)\n- **Type:** Self-hosted multi-agent penetration-testing system.\n- **Purpose:** Coordinates specialized AI agents and 20+ security tools (the README names tools such as Nmap, Metasploit and sqlmap) inside Docker-based execution environments, then produces reports.\n- **Model support:** The README describes multiple hosted providers and local model routes including Ollama and vLLM.\n- **Deployment:** Docker/Compose or Podman guidance; the README lists minimum requirements of 2 vCPU, 4 GB RAM and 20 GB disk.\n- **License:** MIT for the core project, according to the upstream README. VXControl Cloud services may require a separate license key and terms.\n- **Risk classification:** High-impact dual-use security tooling. Sandbox claims do not remove the need for authorization, network isolation, scope limits, and operator oversight. Run only against systems you own or are explicitly authorized to test. Never point autonomous exploitation workflows at public or third-party targets without written authorization.\n- **Assessment:** A specialized red-team / pentest automation platform, not a general coding assistant. Infrastructure and model costs may apply.\n\n## Reader notes

Security tools can cause damage if granted broad access or run against systems without authorization. Audit only repositories and systems you own or are explicitly authorized to assess. Use isolated environments, least privilege, and controlled network access. Recheck upstream instructions before every installation because commands and requirements can change.
