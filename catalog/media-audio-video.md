# Media, Audio and Video

**Catalogue version:** 1.2  
**Last updated:** 2026-11-12 18:29 IST (UTC+05:30)

## Cap

- **Repository:** [capsoftware/cap](https://github.com/capsoftware/cap)
- **Type:** Open-source screen recording and async video collaboration application.
- **Capabilities:** Screen/camera/microphone capture, local editing, share links, comments, transcripts, analytics, team workspaces, custom S3 storage and self-hosting options.
- **AI features:** The README describes AI-generated titles, summaries, chapters, captions and transcripts.
- **Assessment:** Relevant for demos, tutorials, bug reports and asynchronous team communication. Review hosted-service pricing and deployment choices separately.

## WhisperX

- **Repository:** [m-bain/whisperx](https://github.com/m-bain/whisperx)
- **Type:** Speech-recognition and alignment toolkit built around Whisper.
- **Capabilities:** Batched transcription, word-level timestamps, voice activity detection and speaker diarization integrations.
- **Compute:** The README's performance and GPU-memory figures are configuration-specific; do not assume the same throughput on every device.
- **Assessment:** Useful for transcription pipelines, subtitles and diarized audio processing. Check model and dependency licenses and the current compatibility matrix before deployment.

## ManimGX

- **Repository:** [academa-labs/manimgx](https://github.com/academa-labs/manimgx)
- **Type:** Rust/wgpu-powered 3D animation engine with a Manim Community Edition-compatible API, according to its README.
- **Interfaces:** The project advertises Python and npm installation routes and browser-based execution.
- **Assessment:** Promising for mathematical and educational animations. API compatibility should be checked against the exact Manim CE features a project uses.

## Henge

- **Repository:** [alisson-anjos/Henge](https://github.com/alisson-anjos/Henge)
- **Type:** ComfyUI / MiniMax H3-based video studio for character swaps, motion transfer, head swaps and enhancement.
- **Deployment:** The README describes local, RunPod pod and RunPod Serverless workflows, plus an MCP-driven studio assistant.
- **License:** MIT for application code. Model weights, LoRAs, datasets and third-party services have separate terms; the Pika H3 Flex adapter is explicitly not MIT-licensed.
- **Assessment:** Specialized generative-video workflow, not a lightweight general-purpose editor. Compute requirements and model licensing are material constraints.

## Reader notes

Speech and video tools may process faces, voices, biometric-like signals, private conversations, and copyrighted media. Obtain consent and rights where required. Confirm model-weight licenses separately from application-code licenses, and do not infer local/offline operation from an open-source label.
