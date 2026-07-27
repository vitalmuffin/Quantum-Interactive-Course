# Changelog

## v0.16 — architecture stabilization and split loading

- Introduced canonical course configuration and historical data sources.
- Added a reproducible Python build and drift-check command.
- Unified progress into `qm_course_progress_v1` with migration and safe reset.
- Simplified and validated the persistent iframe protocol.
- Split the initial map dataset from lazily loaded paper details.
- Added lazy Plotly loading and modular shared CSS.
- Added explicit, hybrid, and defensive MathJax modes.
- Added numeric, multi-select, ordering, and prediction quiz types.
- Added Chromium, architecture, accessibility, migration, and regression tests.
- Added a short prioritized list of missing principles and primary papers.

## v0.13 — mobile navigation and graph repair

- corrected the stretched spacing of the persistent stage rail;
- removed the redundant stage button from the top bar;
- routed all internal course-stage links through the persistent middle content frame;
- prevented embedded pages from creating a second rail/header;
- replaced graph-template `innerHTML` parsing with SVG template cloning;
- added one-finger pan from any graph point, two-finger pinch zoom, drag-click suppression, and mobile graph sizing;
- moved release documentation and audits into `docs/`;
- packaged the project below the top-level folder `Quantum Interactive Course/`.


## v0.12 — Persistent stage rail, mobile mathematics, graph and translation repair

- Added a persistent collapsible stage rail on the left and content-only stage navigation.
- Kept active-stage highlighting synchronized across page and hash changes.
- Fixed graph node selection and aligned graph/detail panel heights.
- Disabled carousel arrows at their scroll boundaries.
- Replaced remote math rendering with bundled MathJax SVG output and stabilized source-view equations.
- Added seven compact foundation illustrations and removed visible design/meta copy.
- Audited all German translation files; corrected three `_EN` source-language mismatches and added explicit metadata.
- Improved mobile access to stages, progress, sources, tabs, equations, and long paths.


## v0.11 — Offline sources, conceptual stages, model and progress repair

- Renamed course to **Quantum – Das Kleinste verstehen**.
- Pre-rendered the shared header to remove the old-header flash.
- Split the guided journey into ten conceptually defined stages.
- Expanded every primer foundation with plain-language explanations and mini-examples.
- Corrected primer forward navigation and separated overview from prehistory.
- Added pan/zoom controls to the dependency graph.
- Reworked matter-wave, box, uncertainty and molecular models; added the harmonic oscillator.
- Added automatic section progress, repeatable checks and stored knowledge gaps.
- Rebuilt the source reader around a complete offline text bundle and local MathJax.
- Added source-image popovers and contextual captions.
- Passed 40/40 numerical checks and 4/4 runtime smoke tests.

## v0.7

- Repaired and expanded primer patterns 3 and 6.
- Added `math_foundations.html`, `source_reader.html`, and `progress.html`.
- Added selected non-PDF source files from all 32 translated paper folders.
- Added `data/source_index.json` with page-aware equations, blockquotes, and images.
- Added reusable mathematical recall and progress components.
- Added four beginner knowledge checks.
- Updated main navigation and version.

## v0.6

- Added `quantum_information.html`.
- Added nine bilingual interactive laboratories.
- Added qubit-state, gate, entanglement, cloning, teleportation, BB84,
  Deutsch–Jozsa, and Shor simulations.
- Added local primary-source links for Feynman 1982 and Shor 1994.
- Added an explicit system pipeline from encoding to measurement.
- Updated the main navigation and course version.
- Preserved the queued primer issues for the dedicated v0.7 repair pass.

## v0.5

- Added `foundations_tests.html`.
- Added nine bilingual interactive laboratories from EPR to Aspect and decoherence.
- Added finite-sample CHSH simulation with adjustable angles, visibility, pair count, and model.
- Added strict visual separation of theorem, observation, excluded model class, and interpretation.
- Added local links to all relevant primary PDFs and bilingual summaries.
- Added primary-source images for Schrödinger, Kochen–Specker, CHSH, and Aspect.
- Updated the main navigation and course version.
- Did not modify the queued primer issues in patterns 3 and 6.

## v0.4

- Added `historical_core.html` with fourteen bilingual interactive laboratories from Planck to Dirac.
- Added prediction/observation/limitation flow for each historical step.
- Added Temml equations with variable underbraces.
- Added direct links to local PDFs, summaries, and available primary-source images.
- Kept the v0.3.1 primer unchanged; the reported primer issues are deferred.


## v0.3.1

- Fixed Canvas animation trails in all primer simulations.
- Every frame now clears the full device-pixel canvas before redrawing.
- Canvas state such as alpha, compositing, line dashes and shadows is reset.
- High-DPI rendering remains enabled through the restored DPR transform.

## v0.3

- added `primer.html`;
- added bilingual wave laboratory;
- added interactive wave-packet superposition laboratory;
- added Plotly probability and sampling laboratory;
- added complex-plane phasor visualization;
- added spin-½ state/basis probability visualization;
- added derivative/integral Plotly laboratory;
- added operator/eigenstate visualization;
- linked the primer from the main timeline;
- updated project documentation and next-stage plan.

## v0.2

- introduced the 32-paper systems map, timeline, summaries, source images,
  equations, PDFs, dependency graphs and two laboratory prototypes.

## v0.9 — Integrated guided course

- Merged mathematical foundations into the seven primer units.
- Added a shared seven-stage course shell and progress drawer.
- Added a physical prehistory stage before the historical core.
- Moved formulas below all interactive visuals and added symbol-by-symbol legends.
- Rebuilt the source reader for rendered Markdown, excerpts, equations, sources and PDF fallback.
- Added evidence links to every experimental information field.
- Fixed the Bose–Einstein chemical-potential domain and the Planck-only plot scale.
- Added structural, JavaScript runtime and 39-model numerical validation.

## v0.14

- Replaced the fixed mobile stage strip with a small off-canvas navigation trigger.
- Restored the full viewport width for course content on phones.
- Standardized stage-row spacing.
- Replaced MathJax 2 with a self-contained local MathJax 3 SVG bundle.
- Changed dynamic equations to direct asynchronous TeX-to-SVG rendering.
- Updated the source reader to use the same stable renderer.
