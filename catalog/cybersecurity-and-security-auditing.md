# Cybersecurity and Security Auditing

**Catalogue version:** 1.15
**Last updated:** 2026-11-13 02:25 IST (UTC+05:30)

| Project | Classification | Official repository | Status |
|---|---|---|---|
| Cloudflare Security Audit Skill | Coding-agent workflow for repository security auditing | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | Repository identity verified; not a standalone scanner |
| PentAGI | Self-hosted multi-agent penetration-testing platform | [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi) | Repository identity verified; authorized testing only |
| Ghidra | Software reverse-engineering framework | [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra) | Review current upstream LICENSE and release-specific security notices |
| OpenSSL | Cryptographic toolkit and TLS/DTLS/QUIC implementation library | [openssl/openssl](https://github.com/openssl/openssl) | Dual OpenSSL/Apache-2.0 licensing is version-dependent; inspect LICENSE files |

## Cloudflare Security Audit Skill

- **Project link:** [Official source](https://github.com/cloudflare/security-audit-skill)


- **Classification:** Repository-level security auditing skill for coding agents. It is not a standalone vulnerability scanner.

- **License:** MIT, as stated by the upstream project.

- **Purpose:** Structures a security review into reconnaissance, coverage-led hunting, candidate validation, structured findings, independent verification, and reporting.

- **Outputs described by the project:** Architecture and coverage artifacts, machine-readable findings, and human-readable security reports.

- **Finding discipline:** Distinguishes confirmed findings, items needing validation, and rejected candidates. A suspected issue should not be presented as confirmed without evidence of the relevant boundary failure and impact.

- **Installation:** Follow the [official README](https://github.com/cloudflare/security-audit-skill/blob/main/README.md). The documented installation command is:
  
  `npx skills add https://github.com/cloudflare/security-audit-skill --skill security-audit`

- **Operational requirements:** The workflow expects a capable coding agent. The project emphasizes sandboxing and restricted execution for untrusted target code; follow its current safety guidance.

- **Limitations:** It is an audit workflow, not a replacement for professional penetration testing, secure development lifecycle controls, or independent review.

## PentAGI

- **Project link:** [Official source](https://github.com/vxcontrol/pentagi)

- **Type:** Self-hosted multi-agent penetration-testing system.

- **Purpose:** Coordinates specialized AI agents and 20+ security tools (the README names tools such as Nmap, Metasploit and sqlmap) inside Docker-based execution environments, then produces reports.

- **Model support:** The README describes multiple hosted providers and local model routes including Ollama and vLLM.

- **Deployment:** Docker/Compose or Podman guidance; the README lists minimum requirements of 2 vCPU, 4 GB RAM and 20 GB disk.

- **License:** MIT for the core project, according to the upstream README. VXControl Cloud services may require a separate license key and terms.

- **Risk classification:** High-impact dual-use security tooling. Sandbox claims do not remove the need for authorization, network isolation, scope limits, and operator oversight. Run only against systems you own or are explicitly authorized to test. Never point autonomous exploitation workflows at public or third-party targets without written authorization.

- **Assessment:** A specialized red-team / pentest automation platform, not a general coding assistant. Infrastructure and model costs may apply.

## Ghidra

- **Project link:** [Official source](https://github.com/NationalSecurityAgency/ghidra)

- **Type / Classification:** Software reverse-engineering framework.

- **Purpose / Capabilities:** NSA-maintained software reverse-engineering framework for disassembly, decompilation, graphing and scripting across processor architectures and executable formats. Supports interactive and automated analysis.

- **Installation / Requirements:** Runs on Windows, macOS and Linux. Java/Python scripting and extension development are documented upstream; follow the release-specific installation guide.

- **License / Cost:** Confirm current repository license and third-party component terms from the LICENSE files.

- **Privacy / Security / Limitations:** Use current supported releases: upstream README explicitly warns that some versions contain known vulnerabilities. Analyze only software you own or are authorized to inspect; treat untrusted binaries and plugins as hostile.

## OpenSSL

- **Project link:** [Official source](https://github.com/openssl/openssl)

- **Type / Classification:** Cryptographic toolkit and TLS/DTLS/QUIC implementation library.

- **Purpose / Capabilities:** Provides implementations of TLS, DTLS and QUIC plus a general-purpose cryptographic library and command-line utilities. It is foundational infrastructure, not an AI tool.

- **Installation / Requirements:** Build/install instructions and platform support are maintained in the official project documentation; system package managers may provide distribution-specific builds.

- **License / Cost:** OpenSSL project licensing has changed across major versions; inspect the exact release's LICENSE and NOTICE files before redistribution.

- **Privacy / Security / Limitations:** Cryptographic configuration and patch level are security-critical. Prefer supported releases, track advisories, and avoid custom cryptographic designs or unreviewed builds.

## 📝 Note For Reader

Security tools can cause damage if granted broad access or run against systems without authorization. Audit only repositories and systems you own or are explicitly authorized to assess. Use isolated environments, least privilege, and controlled network access. Recheck upstream instructions before every installation because commands and requirements can change.
