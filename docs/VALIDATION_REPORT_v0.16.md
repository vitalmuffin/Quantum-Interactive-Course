# Validierungsbericht v0.16

## Durchgeführte Prüfungen

| Bereich | Ergebnis |
|---|---:|
| HTML-, Link-, Anker- und Quellenpfade | bestanden, 0 Fehler / 0 Warnungen |
| Numerische Modellprüfungen | 40/40 bestanden |
| Runtime-Smoke-Seiten | 4/4 bestanden |
| Deutsche Übersetzungsdateien | bestanden |
| Architektur- und Build-Invarianten | bestanden |
| Migration beider alten Progress-Formate | in Node ausgeführt und bestanden |
| Reset ohne erneuten Altimport | bestanden |
| JavaScript-Syntax der eigenen Runtime-Dateien | bestanden |
| Regressionen v0.12–v0.15 | bestanden |
| Statische Barrierefreiheitsprüfung | bestanden |
| Chromium: MathJax `explicit` | bestanden |
| Chromium: MathJax `hybrid` | bestanden |
| Chromium: MathJax `defensive` | bestanden |
| Chromium: kleine, große und dynamische Formeln | bestanden |
| Chromium: numerische, Multi- und Reihenfolgefragen | bestanden |
| Chromium: mobile Off-Canvas-Navigation | bestanden |

## Leistungsbezogene Strukturprüfungen

- `index.html` liegt unter dem Grenzwert von 450 kB.
- Die vollständige historische Datenbank ist nicht mehr inline eingebettet.
- Das initiale Overview-Bundle liegt unter 100 kB.
- Das vollständige Detailbundle wird erst bei Paperwahl injiziert.
- Plotly wird über einen lokalen Lazy Loader bereitgestellt.
- Scrollfortschritt besitzt eine Mindeständerung vor erneutem Schreiben in Local Storage.

## Grenzen der Prüfung

Die Build-Umgebung blockiert vollständige Navigation zu lokalen HTTP- und `file://`-URLs durch eine Chromium-Administratorrichtlinie. Deshalb wurde die reale gesamte Website nicht per Playwright durchgeklickt. Stattdessen lädt der Browser-Smoke-Test die tatsächlichen Runtime-, CSS- und MathJax-Dateien in eine isolierte Chromium-Seite. Damit werden DOM, SVG, FormData, MutationObserver, Fokus und Responsive-CSS real ausgeführt, nicht nur als Stringmuster geprüft.

Vor einer öffentlichen Kennzeichnung als stabile Version bleiben reale Tests auf mindestens folgenden Geräten sinnvoll:

- Safari auf iPhone;
- Chrome auf Android;
- Firefox auf Android;
- Desktop Firefox;
- GitHub-Pages-Deployment mit Cache-Neuladen und Browser-Zurücknavigation.
