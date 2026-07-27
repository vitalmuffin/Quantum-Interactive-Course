# Release Notes v0.17

## Primer visual corrections

- Sine and cosine are now generated from `Math.sin` and `Math.cos` on one shared coordinate system with the same zero line and the fixed scale −1 to +1.
- The tangent curve uses the same axes but is interrupted outside the visible range instead of drawing false vertical connections across its poles.
- The introductory superposition image now defines two explicit component functions and computes the red curve point by point as `f(x) + g(x)`.
- The interactive wave-packet laboratory also stores every component numerically and draws the bold curve from their literal pointwise sum. Components and sum use one common vertical scale.
- Arrowheads in the static SVG examples and Canvas laboratories were reduced.

## Wave laboratory

- The first wave animation now starts paused. Frequency, wavelength, amplitude, and phase can therefore be compared without the graph moving underneath the controls.
- The spatial snapshot uses a continuously integrated phase. Changing frequency no longer produces an artificial horizontal jump.
- The time trace is centred on the current instant. Frequency changes the number of repetitions in the displayed time interval while the value at “now” stays fixed.

## Complex numbers

- Real part `a = Re(z)` and imaginary part `b = Im(z)` are now the primary inputs.
- The vector, magnitude `|z|`, and phase `arg(z)` are derived from these Cartesian components.
- The Canvas draws the real and imaginary construction steps separately before drawing the resulting complex vector.
- The definition `i = √(−1)` and the equivalent relation `i² = −1` are included explicitly, together with the clarification that `x² = −1` has the two roots `+i` and `−i`.
- Multiplication by `e^{iθ}` remains available as a collapsed optional extension instead of dominating the introductory interaction.

## Range controls

- All native range controls receive a shared Pointer Events fallback.
- Mouse, pen, and touch dragging are captured continuously, including inside the course iframe.
- The controls emit the standard `input` and `change` events, so existing simulations do not need page-specific drag code.
- Slider thumbs were enlarged and now have explicit WebKit and Firefox styling.

## Tests and maintenance

- Added v0.17 regression checks for the corrected plots, literal wave summation, phase-continuous wave behaviour, Cartesian complex controls, `i`, draggable range inputs, and reduced arrowheads.
- Added a Chromium drag test for the shared range implementation.
- Older version-specific cache-buster tests now derive the active version from `data/course.config.json` instead of hard-coding v0.16.
