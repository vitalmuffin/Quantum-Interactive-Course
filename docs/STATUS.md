# Status v0.17

## Platform

**Canonical course configuration:** implemented (`data/course.config.json`)  
**Canonical paper/model data:** implemented (`data/course_data.json`)  
**Reproducible build:** implemented (`tools/build_course.py`)  
**Common page API and validated iframe channel:** implemented  
**Unified progress key:** `qm_course_progress_v1`  
**Migration from both historical progress formats:** tested  
**Modular shared CSS:** implemented  
**Split initial data loading:** implemented  

## Primer corrections

**Sine/cosine common −1…+1 scale:** implemented  
**Mathematically sampled trigonometric plots:** implemented  
**Exact introductory superposition `f+g`:** implemented  
**Pointwise numerical sum in wave-packet Canvas:** implemented  
**Wave laboratory starts paused:** implemented  
**Frequency changes without phase jumps:** implemented  
**Cartesian complex-number controls:** implemented  
**Explicit `i = √(−1)` explanation:** implemented  
**Optional advanced rotation by `e^{iθ}`:** implemented  
**Smaller arrowheads:** implemented  
**Shared draggable range controls:** implemented and Chromium-tested  

## Mathematics and tests

**Local MathJax SVG:** implemented  
**Explicit, hybrid, and defensive modes:** implemented  
**40/40 numerical model checks:** passed  
**4/4 runtime smoke pages:** passed  
**Translation audit:** passed  
**Link and source audit:** passed  
**Accessibility audit:** passed  
**Chromium math, quiz, mobile navigation, and slider-drag fixture:** passed  

## Still open

- Real-device validation on Safari iOS, Chrome Android, and Firefox Android.
- Gradual replacement of legacy page-local simulation code by registered components.
- Further splitting of the large offline source bundle if weak mobile devices still show delays.
- Content extensions only after the selected primary papers have been downloaded and processed.
