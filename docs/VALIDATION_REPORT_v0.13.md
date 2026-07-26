# Validation Report v0.13

## Automated checks

- HTML pages checked: 10
- Local links and source paths checked: 551
- Missing references: 0
- Structural warnings: 0
- Numerical model checks: 40/40 passed
- Runtime smoke pages: 4/4 passed
- German translation-language audit: passed
- v0.12 regression checks: passed
- v0.13 navigation/mobile/folder-structure checks: passed
- Inline JavaScript blocks syntax-checked: 8, errors: 0
- Vendor JavaScript syntax errors: 0

## Browser automation limitation

Chromium navigation to both local HTTP and `file://` URLs is blocked by a system administrator policy in the build environment (`ERR_BLOCKED_BY_ADMINISTRATOR`). Therefore, pixel-level browser automation could not be completed here. The interaction changes are covered by static regression assertions, JavaScript syntax checks, simulated runtime smoke tests, and explicit event-state checks in the implementation.
