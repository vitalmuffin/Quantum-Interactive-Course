# Architektur v0.16

## Ziel

v0.16 stabilisiert die bestehende Iframe-Architektur, ohne die direkte Offline-Nutzung aufzugeben. Inhalt, Navigation, Zustand, Mathematik und Tests erhalten klarere Zuständigkeiten. Die Ausgabe bleibt statisch und kann auf GitHub Pages, über einen lokalen Webserver oder direkt per `file://` verwendet werden.

## Schichten

### 1. Kanonische Daten

`data/course.config.json` ist die einzige Quelle für Kursversion, Etappen, Routen, Fortschrittsschlüssel, Mathematikmodi und zusätzliche Quizfragen.

`data/course_data.json` ist die einzige Quelle für die historische Paper- und Modelldatenbank.

`data/source_index.json` ist die Quelle für verfügbare PDFs, OCR-Seiten, Übersetzungen und extrahierte Abbildungen.

### 2. Build

`tools/build_course.py` erzeugt aus den kanonischen JSON-Dateien:

- `vendor/course-config.js`;
- `data/course_overview.json`;
- `data/course_overview.bundle.js`;
- `data/course_data.bundle.js`;
- `data/papers_index.json` als vorläufige Kompatibilitätsdatei;
- `manifest.json` mit Dateigrößen und SHA-256-Prüfsummen.

`--check` bricht ab, wenn eine generierte Datei nicht mehr zu ihrer Quelle passt.

### 3. Gemeinsame Runtime

`vendor/qm-state.js`
: Versioniertes Zustandsmodell, Migration der beiden alten Progress-Formate, Sprache, Theme und gedrosselte Speicherung des Scrollfortschritts.

`vendor/page-api.js`
: Gemeinsame Schnittstelle für Sprache, Theme, Routen, Kurslinks, Seitenerkennung und Parent/Iframe-Kommunikation.

`vendor/course-shell.js`
: Kopfzeile, Fortschrittsdialog, Quiz-Renderer, Wissenslücken und Vor-/Zurück-Navigation.

`vendor/course-enhancements.js`
: Etappenleiste, Iframe-Lebenszyklus, History-Synchronisierung, mobile Off-Canvas-Navigation und ältere visuelle Ergänzungen.

`vendor/course-data-loader.js`
: Lädt die vollständigen Paperdetails erst bei Bedarf.

`vendor/plotly-loader.js`
: Lädt Plotly erst beim ersten Plot-Aufruf.

### 4. Mathematik

`vendor/math-core.js`
: Normalisierung, MathJax-Bereitschaft, explizites Rendern, Wiederholungsversuche und lesbarer Fallback.

`vendor/math-defensive.js`
: Optionale Beobachtung dynamischer DOM-Änderungen.

`vendor/math-offline.js`
: Öffentliche API und Auswahl zwischen `explicit`, `hybrid` und `defensive`.

## Iframe-Protokoll

Alle Nachrichten tragen:

```javascript
{
  channel: "qm-course-v1",
  type: "navigate" | "location" | "shell-state",
  ...payload
}
```

Der Parent akzeptiert Nachrichten nur vom aktuell eingebetteten Fenster. Bei HTTP(S) muss der Origin dem eigenen Origin entsprechen. Bei `file://` wird der browserübliche opaque/null-Origin zugelassen.

### Parent → Child

`shell-state`
: Sprache und Theme des äußeren Rahmens.

### Child → Parent

`location`
: Aktuelle URL und Etappe nach Laden, Hashwechsel oder relevantem Scrollwechsel.

`navigate`
: Interner Kurslink, der im vorhandenen Iframe geöffnet werden soll.

## Zustandsmodell

```json
{
  "schemaVersion": 1,
  "courseVersion": "0.16",
  "stages": {},
  "sections": {},
  "quizzes": {},
  "papers": {},
  "pages": {},
  "settings": {
    "language": "de",
    "theme": "dark",
    "railExpanded": false
  },
  "migrations": {}
}
```

Der Schlüssel ist `qm_course_progress_v1`. Alte Daten werden einmalig zusammengeführt. Ein Reset entfernt auch die alten Schlüssel.

## Daten-Ladestrategie

Die erste Seite lädt nur etwa 40–50 kB strukturierte Overview-Daten. Darin stehen Module, Abhängigkeiten und die Felder, die Karte, Suche und Paperliste benötigen. Die großen HTML-Zusammenfassungen werden erst beim Öffnen einer Paperkarte geladen.

Diese Trennung reduziert:

- initiale JavaScript-Parse-Zeit;
- Speicherverbrauch auf Mobilgeräten;
- Blockierung des Hauptthreads;
- unnötiges Laden bei Lernenden, die direkt in den geführten Kurs wechseln.

## CSS

`vendor/course-shell.css` ist nur noch ein Einstiegspunkt und importiert:

- `styles/tokens.css`;
- `styles/shell.css`;
- `styles/learning.css`;
- `styles/rail.css`;
- `styles/math.css`.

Neue Regeln sollen in der fachlich passenden Datei ergänzt werden. Versionsspezifische Override-Blöcke am Dateiende sollen nicht erneut aufgebaut werden.

## Quiz-Schnittstelle

Unterstützte Typen:

```text
choice
prediction
multi
number
order
```

Die Fragen werden aus der Konfiguration in den bestehenden Etappenplan eingefügt. Numerische Aufgaben besitzen `answer` und `tolerance`; Mehrfachauswahl und Reihenfolge verwenden `answers`.

## Bekannte Übergangslösungen

- Einige ältere Seitenskripte besitzen weiterhin eigene interne Renderfunktionen. `page-api.js` vereinheitlicht ihre äußere Steuerung; vollständige Komponentenmodule sind ein späterer Schritt.
- `data/papers_index.json` bleibt als Kompatibilitätsalias erhalten. Neue Logik soll ausschließlich `course_data.json` beziehungsweise die generierten Bundles verwenden.
- Der defensive Mathematikmodus bleibt bewusst bestehen, bis genügend reale Browsergeräte den expliziten Weg bestätigt haben.
- Der vollständige Offline-Quellenbundle ist weiterhin groß. Er wird nur in `source_reader.html`, nicht auf der Startseite geladen.
