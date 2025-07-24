# Changelog

## 0.1.0 - Initial Release
- Implemented a basic URL shortener service using Flask.
- Added endpoint to shorten URLs (`POST /api/shorten`).
- Added redirect endpoint (`GET /<short_code>`).
- Added analytics endpoint (`GET /api/stats/<short_code>`).
- In-memory storage for URL mappings and click counts.
- Basic input validation and error handling.
- Wrote initial tests for core functionality.