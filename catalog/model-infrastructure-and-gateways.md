# Model Infrastructure and Gateways

**Catalogue version:** 1.11
**Last updated:** 2026-11-12 21:07 IST (UTC+05:30)

| Project | Classification | Official repository | Status |
|---|---|---|---|
| OmniRoute | Self-hosted multi-provider LLM API gateway and router | [cheaper-inference/OmniRoute](https://github.com/cheaper-inference/OmniRoute) | Repository identity verified; provider quotas and terms are volatile |
| Awesome Free LLM APIs | Directory of free-tier LLM API providers and limits | [open-free-llm-api/awesome-freellm-apis](https://github.com/open-free-llm-api/awesome-freellm-apis) | Repository identity verified; not an API provider or quota guarantee |

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

## 📝 Note For Reader

Treat provider and quota data as a starting point only. Before integrating an API, verify the provider's official pricing and terms, regional access, identity/card requirements, rate limits, model availability, data retention, training use, and commercial-use restrictions. Avoid routing confidential source code or personal data through unknown providers. Keep API keys in a secret manager or environment variables; never...
