# Status v0.16

## Plattform

**Kanonische Kurskonfiguration:** umgesetzt (`data/course.config.json`)  
**Kanonische Paper-/Modelldaten:** umgesetzt (`data/course_data.json`)  
**Reproduzierbarer Build:** umgesetzt (`tools/build_course.py`)  
**Generierte Dateien auf Drift prüfbar:** umgesetzt (`npm run build:check`)  
**Gemeinsame Seiten-API:** umgesetzt (`vendor/page-api.js`)  
**Vereinfachtes und validiertes Iframe-Protokoll:** umgesetzt (`qm-course-v1`)  
**Einheitlicher Fortschrittsschlüssel:** umgesetzt (`qm_course_progress_v1`)  
**Migration aus beiden alten Formaten:** umgesetzt und ausführbar getestet  
**Alte Schlüssel beim Reset entfernt:** umgesetzt  
**Gedrosselte Scrollspeicherung:** umgesetzt  
**Modularisierte gemeinsame CSS-Schicht:** umgesetzt  

## Laden und Mobilgeräte

**`index.html` unter 450 kB:** umgesetzt  
**Kleines initiales Overview-Bundle:** 39 kB komprimierter JavaScript-Text / 48 kB JSON  
**Vollständige Paperdetails erst bei Auswahl:** umgesetzt  
**Plotly erst beim ersten Plot-Aufruf:** umgesetzt  
**Mobile Etappenleiste als Off-Canvas-Overlay:** umgesetzt  
**Keine zweite Shell bei geführter Navigation:** strukturell und im Chromium-Fixture geprüft  

## Mathematik

**Lokales MathJax-SVG:** umgesetzt  
**Expliziter Komponentenmodus:** umgesetzt  
**Hybridmodus als Standard:** umgesetzt  
**Vollständig defensiver Rückfallmodus:** umgesetzt  
**Große und dynamische Formeln in allen drei Modi:** in echtem Chromium geprüft  

## Lernen und Tests

**Multiple Choice:** vorhanden  
**Numerische Aufgaben mit Toleranz:** ergänzt  
**Mehrfachauswahl:** ergänzt  
**Reihenfolgeaufgaben:** ergänzt  
**Vorhersagefragen vor Simulationen:** ergänzt  
**40/40 numerische Modellprüfungen:** bestanden  
**4/4 Runtime-Smoke-Seiten:** bestanden  
**Übersetzungsprüfung:** bestanden  
**Link-/Quellenprüfung:** bestanden  
**Statische Barrierefreiheitsprüfung:** bestanden  
**Chromium-Smoke-Test für Mathematik, Quiz und mobile Navigation:** bestanden  

## Weiter offen

- Reale Endgeräteprüfung auf Safari iOS, Chrome Android und Firefox Android.
- Schrittweise Ablösung älterer seiteninterner Renderfunktionen durch registrierte Komponentenadapter.
- Weitere Aufteilung des großen Offline-Quellenbundles, falls die Quellenansicht auf schwächeren Mobilgeräten weiterhin zu langsam startet.
- Inhaltliche Ergänzungen gemäß `MISSING_PRINCIPLES_AND_PAPERS_v0.16.md` erst nach Download und Quellenprozess.
