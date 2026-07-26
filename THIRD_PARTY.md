# Third-party components

## Plotly.js

- bundled file: `vendor/plotly-3.3.1.min.js`
- upstream project: Plotly.js
- license: MIT
- purpose: interactive scientific plots

## MathJax 2

- bundled directory: `vendor/MathJax/`
- source: MathJax distribution included with the installed Jupyter/nbclassic environment
- license: Apache License 2.0
- purpose: offline TeX rendering in the primary-source viewer

## Graphviz

- used at build time to generate SVG dependency maps
- the Graphviz executable is not bundled
- generated SVG files are included under `data/`
