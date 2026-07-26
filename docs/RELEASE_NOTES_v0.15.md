# Release Notes v0.15

## Behobener Fehler: große Gleichungen blieben als TeX sichtbar

Die nicht gerenderten Formeln waren überwiegend dynamisch erzeugte Display-Gleichungen, etwa Plancks Strahlungsgesetz und die Wellenpaket-Summe. Die kleinen Symbolbeschreibungen waren bereits sichtbar, weil sie normaler Text beziehungsweise Unicode-Zeichen sind und nicht von der TeX-Engine abhängen.

Zwei technische Ursachen wurden behoben:

1. Der gemeinsame Mathematik-Adapter konnte einen Renderaufruf ausführen, bevor die asynchrone MathJax-API vollständig bereitstand. Ein früher Fehler führte dann dauerhaft zur Rohtextdarstellung.
2. Die Quellenansicht übergab Element und Formel in vertauschter Reihenfolge an den gemeinsamen Renderer.

## Änderungen

- Der MathJax-Adapter wartet nun explizit, bis `tex2svgPromise` verfügbar ist.
- Fehlgeschlagene Renderaufrufe werden mit kurzen Verzögerungen wiederholt.
- Äußere Delimiter wie `\[ ... \]`, `\( ... \)` und `$$ ... $$` werden vor der direkten Konvertierung entfernt.
- Der Adapter akzeptiert vorübergehend beide Argumentreihenfolgen, damit ältere Kursmodule nicht ausfallen.
- Dynamisch ergänzte oder verspätet geladene Formeln werden über einen `MutationObserver` erneut erkannt.
- Nach dem Laden erfolgen zwei zusätzliche Sicherheitsdurchläufe für dynamische Inhalte.
- Die großen Formeln in `index.html` und `primer.html` verwenden nun direkt `QMMath.render`.
- Der fehlerhafte Renderaufruf in `source_reader.html` wurde korrigiert.
- Die lokalen MathJax-Skripte besitzen in allen betroffenen Seiten einen Versionsparameter `v=0.15`, damit Browser nicht die alte Adapterdatei aus dem Cache weiterverwenden.

## Betroffene Seiten

- `index.html`
- `primer.html`
- `historical_core.html`
- `foundations_tests.html`
- `quantum_information.html`
- `source_reader.html`

Die Ordnerstruktur aus v0.14 bleibt unverändert.
