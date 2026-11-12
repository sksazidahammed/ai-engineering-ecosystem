# Model Infrastructure and Gateways

**Catalogue version:** 1.12
**Last updated:** 2026-11-12 21:35 IST (UTC+05:30)

| Project | Classification | Official repository | Status |
|---|---|---|---|
| OmniRoute | Self-hosted multi-provider LLM API gateway and router | [cheaper-inference/OmniRoute](https://github.com/cheaper-inference/OmniRoute) | Repository identity verified; provider quotas and terms are volatile |
| Awesome Free LLM APIs | Directory of free-tier LLM API providers and limits | [open-free-llm-api/awesome-freellm-apis](https://github.com/open-free-llm-api/awesome-freellm-apis) | Repository identity verified; not an API provider or quota guarantee |
| OpenJev | Open-source typed-decision inference server with model-serving adapters | [razorback16/openjev](https://github.com/razorback16/openjev) | Apache-2.0 code; hosted quota and model availability are provider-dependent |

## OmniRoute

- **Project link:** [Official source](https://github.com/cheaper-inference/OmniRoute)

- **Type:** Self-hosted LLM API gateway, provider router and compatibility layer.

- **Function:** Routes requests from supported AI coding tools and clients through a unified endpoint to multiple model providers, with configurable strategies and fallback behavior.

- **Provider/free-tier catalogue:** The upstream README advertises hundreds of provider/free-tier entries and a large aggregate monthly token estimate. These are upstream-maintained estimates, not tokens granted by OmniRoute. Provider quotas, signup credits, eligibility, and terms change independently.

- **Operational considerations:** Requires provider credentials and gateway configuration. Self-hosting does not remove provider-side rate limits or data policies. Review logging, credential storage, request routing, fallback behavior and provider terms before sending sensitive code or prompts.

- **Assessment:** Potentially useful for switching providers and centralizing model routing. Do not equate a “free” provider listing with reliable, unrestricted or commercial-use inference.

## Awesome Free LLM APIs

- **Project link:** [Official source](https://github.com/open-free-llm-api/awesome-freellm-apis)

- **Type:** Dynamic directory of free-tier LLM API providers, models, rate limits, context windows, API endpoints and configuration examples.

- **Associated website:** [freellm.net](https://freellm.net), described upstream as a searchable directory and configuration generator.

- **Refresh cadence:** The README states that data is refreshed daily. Counts and provider availability are time-sensitive.

- **Assessment:** Useful for discovering providers and comparing stated constraints. It is not itself an inference API and does not guarantee that any listed provider is accessible from India, remains free, or permits a given use case.

## OpenJev

- **Project link:** [Official source](https://github.com/razorback16/openjev)

- **Type:** Open-source inference server for typed, schema-constrained decisions.

- **Purpose:** Accepts a state plus named yes/no, choice or score questions and returns structured probabilities and confidence values rather than asking an LLM to generate free-form text and parsing the result. It also documents image-based questions and text-generation endpoints.

- **API compatibility:** Implements the TypeSafe Jev `system_one` wire API and an OpenAI-compatible Decisions API endpoint, allowing compatible SDKs to target the server.

- **Models / deployment:** The README lists DiffusionGemma 26B-A4B served through vLLM on NVIDIA GPUs or MLX on Apple silicon, alongside several third-party decision models with their own runtime requirements.

- **Installation / cost:** The README shows a `typesafe-sdk` client and a hosted Codiv endpoint. It advertises a 100-million-input-token free allowance; treat that as a provider offer that may change, not a permanent guarantee. Self-hosting requires substantial model-serving hardware for the larger model.

- **License:** Apache-2.0 for the repository. The README states Apache-2.0 for listed weights, but also includes models maintained by other authors; verify each model's current license and distribution terms separately.

- **Limitations:** The project describes its outputs as probabilities, but those values are not automatically calibrated for every domain or decision. Test calibration, bias, abstention behavior and failure handling before using outputs in consequential workflows.

- **Assessment:** A specialized option for applications that need typed decision outputs and predictable response schemas. It is not a general replacement for a conversational LLM.

## 📝 Note For Reader

Treat provider and quota data as a starting point only. Before integrating an API, verify the provider's official pricing and terms, regional access, identity/card requirements, rate limits, model availability, data retention, training use, and commercial-use restrictions. Avoid routing confidential source code or personal data through unknown providers. Keep API keys in a secret manager or environment variables; never...
