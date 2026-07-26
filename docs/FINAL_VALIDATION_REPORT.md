# Final validation report — v0.8

## Automated integrity checks

- HTML pages checked: 8
- active duplicate HTML IDs: 0
- duplicate IDs inside inert SVG templates: tolerated; only one graph template is mounted at a time
- static missing local references: 0
- missing internal anchors: 0
- unlabelled range controls: 0
- bilingual `data-de` entries without `data-en`: 0
- inline JavaScript syntax errors: 0
- critical browser runtime pages tested: 5
- critical runtime errors after fixes: 0
- PDFs opened successfully: 32 / 32
- source papers indexed: 32
- unique paper IDs: yes
- chronology sorted: yes
- source path, image, equation-page issues: 0
- summary/source text files checked for presence and minimum length: 160
- short or placeholder text findings: 0

## Exceptions

- Active duplicate IDs: none
- Missing references: none
- Missing anchors: none
- Unlabelled sliders: none
- Translation attribute gaps: none
- JavaScript syntax errors: none
- PDF errors: none
- Source/data issues: none
- Text integrity issues: none

## Runtime audit

A Chromium/Playwright harness loaded the course pages with local dependency stubs and exercised the critical probability, calculus, historical, foundations, quantum-information, and source-reader paths. It identified the v0.7 probability failure (`randn` and `gaussian` were undefined). Both functions are now implemented. The source reader was also hardened against missing progress storage and opaque/file test origins.

## Link interpretation

All local link targets exist. PDF anchors such as `#page=N` depend on the browser PDF viewer; the file itself and referenced page range were validated. External CDN availability cannot be guaranteed by a local package.

## External dependency

Plotly is packaged locally. Temml is pinned to 0.13.3 through jsDelivr and has a raw-LaTeX fallback. Fully disconnected equation rendering would require vendoring Temml separately.
