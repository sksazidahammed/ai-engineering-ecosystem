# Local AI and Agent Applications

**Catalogue version:** 1.8  
**Last updated:** 2026-11-12 20:20 IST (UTC+05:30)

| Project | Classification | Official repository | Status |
|---|---|---|---|
| Jan | Desktop application for running local language models | [janhq/jan](https://github.com/janhq/jan) | Repository identity verified; local/offline boundaries need review |
| OpenMausBot | Desktop multi-agent application | [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot) | Repository identity verified; permissions and integrations need review |

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

## 📝 Note For Reader

“Local-first” and “self-hosted” are not synonyms for fully offline or risk-free. Check telemetry, update mechanisms, model-provider routing, app permissions, filesystem access, and whether agents can execute shell commands or control a browser.
