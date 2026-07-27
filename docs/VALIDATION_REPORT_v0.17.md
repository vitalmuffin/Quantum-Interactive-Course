# Validation Report v0.17

## Build and architecture

- Canonical build output: passed.
- Manifest and generated data bundles: rebuilt from `data/course.config.json`, `data/course_data.json`, and `data/source_index.json`.
- Local links, anchors, and source paths: 0 errors, 0 warnings.
- JavaScript syntax checks: passed.
- Progress migration and reset checks: passed.

## Scientific and interaction checks

- Numerical model checks: 40/40 passed.
- Runtime smoke pages: 4/4 passed.
- German translation audit: passed.
- Accessibility audit: passed.
- v0.12–v0.15 regression suites: passed.
- v0.17 primer regression suite: passed.

The v0.17 suite verifies that:

1. sine and cosine share a centred −1…+1 scale;
2. the red introductory superposition curve is computed as `f(x)+g(x)`;
3. the interactive packet curve is the pointwise sum of its stored components;
4. changing frequency does not introduce a phase jump and the wave starts paused;
5. the complex vector is constructed from real and imaginary inputs;
6. `i = √(−1)` and `i² = −1` are present with the `±i` root clarification;
7. range controls can be dragged continuously through the shared Pointer Events layer;
8. SVG and Canvas arrowheads use the reduced sizes.

## Chromium checks

The isolated Chromium suite passed for:

- explicit, hybrid, and defensive MathJax modes;
- large and dynamically inserted equations;
- one generated shell and one stage rail;
- advanced quiz controls;
- desktop and mobile off-canvas navigation;
- continuous mouse dragging of an enhanced range input.

Direct navigation to `http://127.0.0.1` and `file://` remains blocked by an administrator policy in the build environment (`ERR_BLOCKED_BY_ADMINISTRATOR`). The browser suite therefore injects the real local scripts and styles into Chromium. Final checks on Chrome Android and Safari iOS remain necessary because the original slider problem occurred on real touch devices.
