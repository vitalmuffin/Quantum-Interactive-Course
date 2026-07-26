# Validierungsbericht v0.15

## Schwerpunkt

Geprüft wurde die direkte SVG-Konvertierung großer, dynamisch erzeugter TeX-Gleichungen sowie die erneute Verarbeitung verspätet eingefügter Formeln.

## Browsernaher Isolationstest

Der lokal gebündelte MathJax-3-Code und `vendor/math-offline.js` wurden in einer isolierten Chromium-Seite geladen. Erfolgreich zu SVG konvertiert wurden unter anderem:

- Plancks Strahlungsgesetz;
- die Summe eines Wellenpakets;
- eine Formel mit äußeren `\[ ... \]`-Trennzeichen;
- ein Aufruf mit der früher vertauschten Argumentreihenfolge der Quellenansicht;
- eine erst nachträglich über `data-tex` erkannte Formel.

Bei allen Testelementen entstand ein `mjx-container` ohne `qm-math-error`.

## Automatisierte Paketprüfungen

- lokale Links und Quelldateien;
- mathematische Modelltests;
- Runtime-Smoke-Tests;
- Übersetzungsprüfung;
- Feature-Regressionen v0.12 bis v0.15;
- JavaScript-Syntax des gemeinsamen Mathematik-Adapters;
- Vorhandensein der cache-aktualisierten lokalen MathJax-Verweise.

Eine vollständige pixelbasierte Navigation durch die lokal bereitgestellten Kursseiten blieb in der Build-Umgebung durch die systemweite Chromium-URL-Sperrrichtlinie blockiert. Der isolierte MathJax-Lauf selbst konnte jedoch direkt in Chromium ausgeführt werden.
