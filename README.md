# Quantum – Das Kleinste verstehen · v0.16

Ein bilingualer, interaktiver Kurs zur Entwicklung der Quantenmechanik. Die primäre Zielgruppe sind STEM-Einsteiger:innen. Kurze Erklärungen, Modelle und Verständnischecks bilden den geführten Weg; Primärquellen und ausführliche Aufbereitungen stehen als direkte Vertiefung daneben.

## Start

Direkt und offline:

```bash
https://vitalmuffin.github.io/Quantum-Interactive-Course/foundations_tests.html
```

oder über folgende URL erreicht werden:
```bash
cd 'Quantum Interactive Course'
./start_course.sh
```

Über einen lokalen Webserver:

```bash
./start_course.sh
```

Danach `http://localhost:8000/` öffnen. Der Kurs bleibt mit `file://` kompatibel; der lokale Server ist für Entwicklung und Browser-Debugging bequemer.

## Kursstruktur

1. Überblick und historische Systemkarte
2. Grundlagen und mathematischer Primer
3. Klassische Grenzen
4. Energiequanten und Photonen
5. Materiewellen und Statistik
6. Operatoren und Wellenmechanik
7. Wahrscheinlichkeit, Bindung und Felder
8. Deutung und experimentelle Tests
9. Quanteninformation
10. Primärquellen

Die Seitenleiste wird aus einer gemeinsamen Konfiguration erzeugt. Auf Mobilgeräten liegt sie außerhalb des Inhaltsbereichs und wird über ein kleines Menüsymbol geöffnet. Kurswechsel erfolgen im bestehenden Iframe-Rahmen; es wird keine zweite Shell erzeugt.

## Architektur in v0.16

### Eine Quelle der Wahrheit

Manuell gepflegte Kerndaten:

```text
data/course.config.json   Kursversion, Etappen, Routen, Zustandsschlüssel, Quiz-Erweiterungen
data/course_data.json     Paper-, Modell- und Abhängigkeitsdaten
data/source_index.json    Dateien und Metadaten der Quellenansicht
```

Generierte Dateien dürfen nicht direkt bearbeitet werden:

```text
vendor/course-config.js
data/course_overview.json
data/course_overview.bundle.js
data/course_data.bundle.js
data/papers_index.json
manifest.json
```

### Geteiltes Laden

`index.html` enthält die große Paper-Datenbank nicht mehr. Für Karte, Filter und Paperliste wird zunächst nur das kleine Overview-Bundle geladen. Vollständige Zusammenfassungen, Gleichungen und Quelldetails werden erst beim Öffnen eines Papers über `vendor/course-data-loader.js` nachgeladen. Das reduziert Parse-Arbeit und Speicherbedarf beim ersten Seitenaufbau.

Plotly wird ebenfalls erst beim ersten Plot-Aufruf aus dem lokalen Bundle geladen.

### Gemeinsame Seitenschnittstelle

`vendor/page-api.js` stellt die gemeinsame Schnittstelle für alle Seiten bereit:

- Sprache und Theme setzen;
- aktuelle Etappe aus Route und Anker bestimmen;
- Kurslinks normalisieren;
- Parent/Iframe-Nachrichten über den Kanal `qm-course-v1` senden;
- Nachrichtenquelle und Origin prüfen;
- seitenabhängige Adapter registrieren.

`vendor/course-enhancements.js` enthält den äußeren Iframe-Rahmen und die Etappenleiste. `vendor/course-shell.js` erzeugt Kopfzeile, Fortschritt, Etappenquiz und Dialoge.

### Fortschritt

Der kanonische Local-Storage-Schlüssel lautet:

```text
qm_course_progress_v1
```

Beim ersten Start werden die älteren Formate `quantum_course_progress_v011` und `qm_course_progress_v07` zusammengeführt. Danach wird nur das neue Schema verwendet. Beim Zurücksetzen werden auch die alten Schlüssel entfernt, damit gelöschter Fortschritt nicht erneut importiert wird.

Scrollfortschritt wird nur bei einer relevanten Zunahme gespeichert, nicht bei jedem einzelnen Scroll-Frame.

### Mathematik

Die MathJax-SVG-Ausgabe ist lokal gebündelt. Drei Modi stehen bereit:

```text
?math=explicit    nur gezielte Komponentenaufrufe
?math=hybrid      gezielte Aufrufe plus Beobachtung neu eingefügter Formelbereiche; Standard
?math=defensive   zusätzliche vollständige Nachprüfung und Wiederholungsversuche
```

Die gemeinsame API lautet:

```javascript
await window.QMMath.render(tex, element, { displayMode: true });
await window.QMMath.renderMarked(rootElement);
```

Der defensive Modus bleibt als Vergleichs- und Rückfalloption erhalten, bis der explizite Komponentenweg auf allen Zielbrowsern ausreichend erprobt ist.

## Verständnischecks

Neben Multiple-Choice-Fragen unterstützt der gemeinsame Quiz-Renderer:

- numerische Antworten mit Toleranz;
- Mehrfachauswahl;
- Reihenfolgeaufgaben;
- Vorhersagefragen vor einer Simulation.

Die zusätzlichen Aufgaben werden in `data/course.config.json` gepflegt und automatisch den passenden Etappen zugeordnet.

## Build

Der Build verwendet nur die Python-Standardbibliothek:

```bash
npm run build
```

Der Befehl erzeugt die Runtime-Konfiguration, die beiden Daten-Bundles, den Kompatibilitätsindex und das Manifest neu.

Prüfen, ob generierte Dateien aktuell sind:

```bash
npm run build:check
```

## Tests

Vollständige Prüfung:

```bash
npm test
```

Enthalten sind:

- lokale Links, Anker und Quellenpfade;
- 40 unabhängige numerische Modellprüfungen;
- Übersetzungsprüfung der deutschen Quelldateien;
- Runtime-Smoke-Tests der Modellseiten;
- Architektur-, Build- und Migrationsinvarianten;
- statische Barrierefreiheitsprüfung;
- Regressionstests für die Änderungen aus v0.12–v0.15;
- echte Chromium-Tests für alle drei Mathematikmodi, Quiztypen und die mobile Off-Canvas-Navigation.

Die Browser-Smoke-Tests verwenden eine injizierte Testseite, weil lokale HTTP- und `file://`-Navigation in manchen Build-Umgebungen durch Chromium-Richtlinien gesperrt sein kann.

## Verzeichnisstruktur

```text
assets/       Bilder und weitere Kursressourcen
data/         kanonische Daten und generierte Browser-Bundles
docs/         Architektur, Audits, Roadmap und Release Notes
sources/      Primärquellen, OCR-Seiten, PDFs und Extraktionen
summaries/    deutsche und englische Aufbereitungen
tests/        statische, numerische, Runtime- und Browserprüfungen
tools/        reproduzierbarer Build
vendor/       gemeinsame Runtime, CSS und lokal gebündelte Bibliotheken
```

## Nächste inhaltliche Erweiterungen

Die priorisierte, bewusst kurze Paperliste steht in:

```text
docs/MISSING_PRINCIPLES_AND_PAPERS_v0.16.md
```

Neue Papers sollten zuerst heruntergeladen, rechtlich geprüft, extrahiert, übersetzt und durch denselben bestehenden Quellenprozess geführt werden. Erst danach werden sie in `data/course_data.json` aufgenommen.
