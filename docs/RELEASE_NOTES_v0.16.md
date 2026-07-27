# Release Notes v0.16 — Architektur-Stabilisierung

v0.16 ist kein weiterer reiner Patch einzelner Darstellungen. Die Version konsolidiert die Plattform, damit spätere Inhalte nicht erneut mehrere voneinander abweichende Daten-, Navigations- und Fortschrittssysteme erzeugen.

## Eine Quelle der Wahrheit

- `data/course.config.json` steuert Version, Etappen, Routen, Zustandsschlüssel, Mathematikmodi und zusätzliche Quizfragen.
- `data/course_data.json` ist die kanonische historische Datenbank.
- Laufzeit-Bundles, Kompatibilitätsindex und Manifest werden daraus erzeugt.
- Doppelte Stage-Arrays in Shell und Enhancements wurden entfernt.

## Build

- Neuer reproduzierbarer Build: `tools/build_course.py`.
- `npm run build` regeneriert alle abgeleiteten Dateien.
- `npm run build:check` erkennt Drift zwischen Quelle und Ausgabe.
- `manifest.json` enthält Dateigrößen und SHA-256-Prüfsummen.

## Schnellere Startseite

- Die große Datenbank wurde aus `index.html` entfernt.
- Die Startseite lädt zunächst nur ein Overview-Bundle von ungefähr 40 kB.
- Vollständige Paperzusammenfassungen und Detailfelder werden erst beim Öffnen eines Papers geladen.
- Plotly wird erst beim ersten Plot-Aufruf geladen.

## Zustand und Fortschritt

- Neuer kanonischer Schlüssel `qm_course_progress_v1`.
- Automatische Zusammenführung von `quantum_course_progress_v011` und `qm_course_progress_v07`.
- Reset entfernt alte Schlüssel, damit gelöschte Daten nicht erneut importiert werden.
- Scrollfortschritt wird nicht mehr bei jedem Frame gespeichert.

## Iframe und gemeinsame Seiten-API

- Gemeinsamer Nachrichtenkanal `qm-course-v1`.
- Validierung von Nachrichtenquelle und Origin.
- Ein Route-/Sprach-/Theme-Interface für alle Seiten.
- Nur ein äußerer Iframe, eine Etappenleiste und eine Shell.
- Mobile Etappenleiste bleibt vollständig außerhalb der Inhaltsbreite.

## CSS

Die gemeinsame CSS-Datei wurde in Tokens, Shell, Lernkomponenten, Etappenleiste und Mathematik aufgeteilt. Wiederholte versionsspezifische Override-Schichten wurden durch klarere Zuständigkeiten ersetzt.

## Mathematik

Drei auswählbare Modi:

- `explicit` für gezieltes Rendern durch Komponenten;
- `hybrid` als Standard mit gezielter Beobachtung neu eingefügter Formelbereiche;
- `defensive` mit vollständiger Nachprüfung und zusätzlichen Wiederholungsversuchen.

Alle drei Modi wurden mit kleinen, großen und dynamisch eingefügten Formeln in Chromium ausgeführt.

## Quiztypen

Zusätzlich zu den bisherigen Fragen:

- numerische Aufgaben mit Toleranz;
- Mehrfachauswahl;
- Reihenfolgeaufgaben;
- Vorhersagefragen vor der Parameteränderung einer Simulation.

Acht zusätzliche Fragen liegen in der kanonischen Kurskonfiguration.

## Barrierefreiheit

- Labels für Such- und Filterfelder ergänzt.
- Fokus wird in Kursdialogen gehalten und nach dem Schließen wiederhergestellt.
- Dialogzustand über `aria-hidden` sichtbar gemacht.
- einheitliche `:focus-visible`-Markierung;
- `prefers-reduced-motion` berücksichtigt.

## Inhaltliche Planung

`docs/MISSING_PRINCIPLES_AND_PAPERS_v0.16.md` priorisiert fünf Ergänzungen: Spin/Stern–Gerlach, Davisson–Germer, Tunneln, Dichteoperator und Dekohärenz. Die Liste ist bewusst kurz und setzt voraus, dass neue Quellen zuerst durch den bestehenden Download-, Extraktions-, Übersetzungs- und Auditprozess laufen.
