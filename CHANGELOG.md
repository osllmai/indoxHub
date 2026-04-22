# Changelog

All notable changes to IndoxHub Python Client will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2026-04-22

### Added

- **Resemble AI namespace** at `client.resemble.*` covering 13 endpoint groups (~67 endpoints):
  text-to-speech (sync synth, voice listing), speech-to-text (async jobs),
  audio enhance + edit, deepfake detection / content intelligence / audio
  source tracing, watermark apply + detect, identity (beta) search/enroll/CRUD,
  voice cloning + voice design (Business-plan gated), recordings (training audio),
  projects + nested clips, agents + tools + webhooks + knowledge base, file uploads.
- `ResembleBusinessPlanError` exception raised when the deployment's
  `RESEMBLE_BUSINESS_PLAN_ACTIVE` flag is off and a gated capability is called.
- 77 unit tests covering every Resemble method (mocked).

### Notes

- BYOK is not supported on Resemble routes (server uses a single account key).
- WebSocket TTS streaming and live agent dispatch are intentionally not exposed.

## [0.1.40]

### Changed

- Package name changed from `indoxrouter` to `indoxhub`

## [0.1.39] - 2025-11-09

### Added

- Video generation via API support
- New image models integration

### Added

- Video generation support with multiple providers (OpenAI, Google, Amazon)
- Asynchronous video processing with job status tracking
- Enhanced image generation with provider failover
- Better error handling and retry logic
- Improved logging and debugging capabilities
