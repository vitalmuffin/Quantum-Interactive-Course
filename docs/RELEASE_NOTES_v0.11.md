# Release Notes v0.11

- Fehler im Startseiten-Initialisierer behoben; der Systemgraph lädt wieder und bleibt zoombar/verschiebbar.
- Horizontale Kursnavigation durch eine kompakte obere Leiste und eine ausklappbare Etappen-Seitenleiste ersetzt.
- Einführung besitzt keinen Verständnischeck mehr.
- Mathematische Grundbegriffe sind kompakt; ausführliche Erklärungen öffnen sich erst nach Klick. Der interne Drei-Quellen-Vergleich ist aus der Lernansicht entfernt.
- Primer-Quiz auf drei Fragen reduziert; falsche Antworten zeigen ausführliche Erklärungen und Rücklinks.
- Quizze öffnen nicht mehr automatisch beim Scrollen, sondern nur über Endkarten oder den Fortschrittsbereich.
- Historische Jahresnavigation als Carousel mit Pfeiltasten umgesetzt.
- Quellenviewer: Markdown-Tokenisierung und Inline-LaTeX korrigiert; OCR-Rohformeln werden bei unsicherer Syntax nicht mehr blind an MathJax übergeben.
- Primärquellenbilder bleiben in Popovers mit Bildunterschrift und Seitenkontext.


## Validierung

- 40/40 numerische Modellprüfungen bestanden.
- 4/4 Runtime-Smoke-Tests bestanden.
- 532 lokale Verweise und 32 Quellenpakete ohne Fehler geprüft.
- Kontrollierte Chromium-Prüfung für Systemgraph, Primer-Quiz, historische Carousel-Navigation und Quellenansicht durchgeführt.
