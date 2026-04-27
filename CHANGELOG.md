# Changelog

All notable changes to IndoxHub Python Client will be documented in this file.



## [0.2.1] - 2026-04-27

### Added

- **R2 mirror surface** — Resemble responses now expose `audio_url` (presigned
  Cloudflare R2 URL) and `expires_at` (ISO 8601 timestamp). Affected methods:
  `tts.synthesize`, `audio_jobs.get_enhance` / `get_edit`, `watermark.get_apply`.
  Mirroring is server-side, lazy + idempotent — first GET after job completion
  writes to R2, subsequent GETs return the same R2 URL.
- **`uploads.create(file_path, purpose=None)`** — new `purpose` parameter
  controls retention. Pass `purpose="voice_clone"` to land voice-clone source
  recordings under `voice-recordings/` with **PERMANENT** retention. Other
  values: `stt_input` (30d), `watermark_input` (7d), `audio_job_input` (7d).
  Default (no purpose): `uploads/` prefix, 30-day retention.
- Docstring updates noting the new fields and per-asset retention model.

### Changed

- Maintainer email: `support@indoxhub.com`.

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
