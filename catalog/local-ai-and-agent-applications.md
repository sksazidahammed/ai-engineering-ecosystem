# Local AI and Agent Applications

**Catalogue version:** 1.15
**Last updated:** 2026-11-13 02:25 IST (UTC+05:30)

| Project | Classification | Official repository | Status |
|---|---|---|---|
| Jan | Desktop application for running local language models | [janhq/jan](https://github.com/janhq/jan) | Repository identity verified; local/offline boundaries need review |
| OpenMausBot | Desktop multi-agent application | [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot) | Repository identity verified; permissions and integrations need review |
| watermarks-remover | Agent skills and local Python HTTP service for inspecting and cleaning AI provenance marks in text and files | [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | MIT; statistical rewriting and pixel/audio/video backends have important limits |

## Jan

- **Project link:** [Official source](https://github.com/janhq/jan)

- **Type:** Desktop application for downloading and running open-source language models with local control.

- **Platforms:** The README lists Windows, macOS and Linux distribution paths.

- **Assessment:** A practical graphical entry point for local LLM experimentation. Model size, RAM/VRAM, quantization and inference speed determine whether a particular machine can run a model comfortably. Local inference does not automatically mean every connected feature is offline.

## OpenMausBot

- **Project link:** [Official source](https://github.com/milind-soni/OpenMausBot)

- **Type:** Desktop multi-agent application for managing AI bots through a chat-style interface.

- **Architecture described upstream:** Individual agents can use different models and connected applications, with local desktop execution and approval-oriented workflows.

- **Platforms shown in README:** macOS, Windows and Ubuntu/Linux.

- **Assessment:** Interesting personal-agent / agent-team interface. Inspect the actual permissions, computer-use boundaries, connected-app scopes, model-provider data flows and approval controls before connecting accounts or allowing actions.

## watermarks-remover

- **Project link:** [Official source](https://github.com/guillaumemeyer/watermarks-remover)

- **Type:** Two agent skills plus a Python HTTP service, CLI utilities and a Claude Code plugin/marketplace. It is not a standalone desktop watermark-removal application.

- **Purpose:** Inspects and cleans invisible Unicode characters, selected statistical text-watermark patterns, and provenance or metadata marks in supported files. The repository explicitly frames its intended use as privacy and hygiene for content the user owns.

- **Workflow:** Layer A deterministically handles invisible Unicode, exotic spaces, bidirectional controls and tag characters. Layer B uses agent-assisted rewriting and optional rewrite backends for statistical token-sampling marks. File cleaning targets C2PA, EXIF, XMP and document properties across image, document, web, audio and video formats. The agent skill is a thin HTTP client; the cleaning engine runs in the separate service.

- **Installation:** Python 3.10+ is listed for the standard-library skill installer. Install a skill with `python3 install_skill.py --skill remove-ai-marks --target codex` (or choose a supported target such as Claude Code or Cursor). Start the service separately with `make serve` or Docker Compose; the default endpoint is `http://127.0.0.1:8765`. The repository also documents a Claude Code plugin marketplace installation.

- **Integrations:** The README lists Claude Code, Codex, Cursor and Cowork/claude.ai skill targets, plus an HTTP API with `/health`, `/capabilities`, `/inspect`, `/detect` and `/clean` endpoints. Optional tools and heavy detection/removal backends must be configured on the service host.

- **License:** MIT for the repository. Optional external tools, model weights, detector/scorer backends and third-party services may have separate licenses or terms.

- **Privacy / security:** The service can process uploaded file contents and may be exposed beyond loopback if configured. Keep it bound to localhost unless remote access is required; use HTTPS and API-key protection for remote connections, restrict network access, and avoid sending confidential files to untrusted hosts or external rewrite/detection providers. Review plugin hooks before enabling automatic cleaning.

- **Limitations:** Metadata stripping is not equivalent to removing every form of provenance. C2PA soft bindings and data-driven/backdoor marks are out of scope. Optional SynthID, MarkLLM, pixel, audio and video capabilities depend on separately configured backends. The README explicitly describes audio processing as destructive and video removal as partial; outputs may be altered. A successful clean does not prove that content was human-written or that every detector will return a negative result.

- **Assessment:** A broad, technically ambitious local-first toolkit for auditing and cleaning provenance metadata on files you own. Treat it as a privacy/metadata utility, not a way to establish authorship or bypass disclosure obligations.

## 📝 Note For Reader

“Local-first” and “self-hosted” are not synonyms for fully offline or risk-free. Check telemetry, update mechanisms, model-provider routing, app permissions, filesystem access, and whether agents can execute shell commands or control a browser.
