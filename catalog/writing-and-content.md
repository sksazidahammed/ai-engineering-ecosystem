# Writing and Content

**Catalogue version:** 1.8  
**Last updated:** 2026-11-12 20:20 IST (UTC+05:30)

| Project | Provisional classification | Source | Status |
|---|---|---|---|
| OpenMontage | Agentic video-production system | [OpenMontageInc/OpenMontage](https://github.com/OpenMontageInc/OpenMontage) | Verified identity; AGPL-3.0 stated upstream |
| HyperFrames | HTML/CSS/media-to-video framework with agent support | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | Verified identity; Apache-2.0 stated upstream |
| Humanizer | Writing skill / text transformation | [blader/humanizer](https://github.com/blader/humanizer) | Verified identity; does not claim reliable AI-detector evasion |
| I Have ADHD | Concise, action-first coding-agent response-style skill | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | Verified identity; not a clinical/diagnostic tool |
| Marketing Skills | Marketing-focused agent skills for CRO, copywriting, SEO, analytics and growth | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | Verified identity; MIT stated upstream |
| Harper | Local-first English grammar checker and language tooling | [automattic/harper](https://github.com/automattic/harper) | Verified identity; English-only stated upstream |

## OpenMontage

- **Project link:** [Official source](https://github.com/OpenMontageInc/OpenMontage)

- **Type:** Agentic video-production application for planning and producing videos from natural-language direction.

- **Workflow:** The upstream project describes a pipeline covering research, script development, asset sourcing, editing and rendering. The exact amount of automation depends on connected providers and the configured workflow.

- **License:** AGPL-3.0, as stated upstream. Review its obligations before modifying the software or offering a network-hosted derivative.

- **Practical considerations:** Check the rights and licenses for sourced footage, music, images and other assets. Model/API usage, storage and rendering may introduce costs.

## HyperFrames

- **Project link:** [Official source](https://github.com/heygen-com/hyperframes)

- **Type:** HTML/CSS/media-to-video framework with command-line and coding-agent workflows.

- **Purpose:** Builds deterministic MP4 videos from web-native layouts, media and seekable animations rather than relying on a traditional nonlinear-editing timeline.

- **Requirements:** Node.js 22+ is stated upstream; rendering also depends on the browser/runtime and available system resources.

- **License:** Apache-2.0, as stated upstream.

- **Practical considerations:** Test font loading, timing, asset paths and render reproducibility in the target environment. It is suited to programmatic video production, not a drop-in replacement for every desktop video editor.

## Humanizer

- **Project link:** [Official source](https://github.com/blader/humanizer)

- **Type:** Writing skill that revises AI-generated prose to remove formulaic patterns and improve naturalness.

- **Important limitation:** The README explicitly says it is not designed to bypass AI detectors and that detectors may still flag its output. Do not use it to misrepresent authorship or guarantee detector evasion.

## I Have ADHD

- **Project link:** [Official source](https://github.com/ayghri/i-have-adhd)

- **Type:** Coding-agent style skill that prioritizes the next action, numbered steps, concise output and one concrete next step.

- **Assessment:** A communication preference pack, not an ADHD assessment, treatment or clinical tool.

## Marketing Skills

- **Project link:** [Official source](https://github.com/coreyhaines31/marketingskills)

- **Type:** Collection of agent skills for conversion optimization, copywriting, SEO, analytics and growth engineering.

- **Integrations:** The README includes optional workflows for connecting marketing accounts and a disclosed partner registry. Review requested scopes and partner disclosures before connecting accounts.

- **License:** MIT, according to upstream.

- **Assessment:** Useful for technical marketers and founders; it is a skill library, not a complete autonomous marketing platform.

## Harper

- **Project link:** [Official source](https://github.com/automattic/harper)

- **Type:** English grammar checker and language tooling, including editor integrations and WebAssembly support.

- **Design:** The upstream project describes it as privacy-focused and designed for fast local linting.

- **Language support:** English only, according to the current README.

- **Assessment:** Useful for proofreading and writing feedback; it is not a generative writing assistant or a general-purpose multilingual grammar checker.

## 📝 Note For Reader

Writing and content tools may produce inaccurate claims, synthetic media, or content that resembles existing work. Check factual statements, attribution, privacy implications, and the applicable license or platform rules before publishing generated output.
