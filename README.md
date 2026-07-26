# Quantum – Das Kleinste verstehen · v0.12

Ein bilingualer, interaktiver Onlinekurs zur Entwicklung der Quantenmechanik. Der Kurs verbindet mathematische Grundlagen, Primer, physikalische Vorgeschichte, historische Primärarbeiten, Modellrechnungen, Grundlagenexperimente und Quanteninformation zu einem geführten Lernweg.

## Start

Die Startseite kann direkt geöffnet werden:

```bash
xdg-open index.html
```

Die Quellenansicht ist in v0.12 vollständig offline gebündelt und funktioniert ebenfalls beim direkten Öffnen über `file://`.

Optional kann der Kurs über einen lokalen Webserver gestartet werden:

```bash
cd qm_interactive_course_v0.12
./start_course.sh
```

Danach im Browser öffnen:

```text
http://localhost:8000/
```

## Geführter Lernweg

1. **Überblick** — Systemkarte, zwei interaktive Einstiegsmodelle und Motivation.
2. **Grundlagen & Primer** — sieben Konzepte mit Definitionen, Mini-Beispielen, Abbildungen und interaktiven Modellen.
3. **Klassische Grenzen** — Mechanik, Elektrodynamik, Thermodynamik und die messbaren Krisen vor der Quantenmechanik.
4. **Energiequanten & Photonen** — Planck, Einstein, Bohr, Strahlungsprozesse und Compton.
5. **Materiewellen & Statistik** — de Broglie, Bose–Einstein, Fermi–Dirac und Pauli.
6. **Operatoren & Wellenmechanik** — Matrixmechanik, Schrödinger-Gleichung und harmonischer Oszillator.
7. **Wahrscheinlichkeit, Bindung & Felder** — Born-Regel, Unschärfe, Molekülbindung, Feldquantisierung und Dirac.
8. **Deutung & Tests** — EPR, Katze, Bohm, Everett, Bell, CHSH, Kochen–Specker, Aspect und Dekohärenz.
9. **Quanteninformation** — Qubits, Gatter, Verschränkung, No-Cloning, Teleportation, BB84, Deutsch–Jozsa und Shor.
10. **Quellen** — 32 Primärarbeiten mit formatierter Aufbereitung, OCR-Seiten, Gleichungen, Abbildungen und PDFs.

Die obere Kursleiste ist bereits im HTML vorhanden und wird nicht erst nachträglich aufgebaut. Dadurch erscheint beim Seitenwechsel kein alter Header. Der DE/EN-Umschalter bleibt als segmentierter Schalter erhalten.

## Mathematik und Primer

`primer.html` enthält sieben Einheiten:

- Funktionen, Wellen und Wellenpakete;
- Superposition;
- Wahrscheinlichkeit, Normierung, Erwartungswert und Varianz;
- komplexe Zahlen und Phase;
- Zustände und Messbasen;
- Ableitung und Integral;
- Operatoren, Eigenvektoren und Eigenwerte.

Jede Einheit enthält kurze Definitionen, anschauliche Erklärungen, Mini-Beispiele und eine passende Abbildung. Vertiefungen können bei Bedarf aufgeklappt werden.

Historische Texte verlinken zum passenden Primer. Über den Rückkehrparameter gelangt man anschließend wieder zur ursprünglichen Textstelle. Die Abschlusskarten des Primers führen nun zu den zugehörigen historischen Modellen; der primäre Weiter-Button führt in die Vorgeschichte.

## Interaktive Modelle

Der historische Kern enthält 15 Modelle. Neu oder grundlegend überarbeitet wurden insbesondere:

- Materiewellen-Doppelspalt mit festem Schirmausschnitt, sodass steigende Masse beziehungsweise steigender Impuls die Fransen sichtbar verkleinert und schließlich unter die Auflösung drückt;
- Teilchen im Kasten mit `ψ` als Standardansicht und deutlich markierten unendlichen Wänden;
- harmonischer Oszillator mit Potential, Energieniveaus, Zustandsbreite und Knotenzahl;
- Unschärferelation als direkter Breitentausch zwischen Orts- und Impulsverteilung;
- Molekülbindung mit Kernabstoßung für `R → 0`, massenabhängigen Vibrationsabständen und einer zusätzlichen Atomschemadarstellung.

Formeln stehen unter den Visualisierungen. Formelzeichen werden in separaten Zeilen erklärt; horizontales Scrollen und überladene Underbrace-Beschriftungen wurden entfernt.

## Fortschritt und Verständnischecks

- Der Lesefortschritt wird beim Scrollen automatisch gespeichert.
- Historische Unteretappen besitzen jeweils einen eigenen lokalen Scrollfortschritt.
- Nach jedem inhaltlichen Abschnitt steht eine wiederholbare Verständnisfrage.
- Am Ende einer Etappe öffnet sich einmalig der Etappentest, sofern die Etappe noch nicht abgeschlossen ist.
- Falsche Antworten werden als Wissenslücken im Fortschritts-Pop-out gespeichert und verlinken zurück zur relevanten Textstelle beziehungsweise Darstellung.
- Ein Abschnitt gilt erst nach richtiger Antwort als verstanden; Tests können jederzeit wiederholt werden.

## Quellenansicht

`source_reader.html` verwendet `data/source_offline_bundle.js`. Darin sind der vollständige Quellenindex und 748 lokale Textdateien eingebettet. Es ist kein `fetch()` für Zusammenfassungen, OCR-Seiten oder Übersetzungen erforderlich.

Verfügbar sind:

- formatierte Kursaufbereitung;
- seitenweiser Paper-Ausschnitt;
- Original-OCR sowie deutsche und englische Fassungen; bei drei englischen Übersetzungen ursprünglich deutscher Arbeiten wird statt einer nicht verlässlichen deutschen Volltextübersetzung transparent eine geprüfte deutsche Aufbereitung angezeigt;
- Schlüsselgleichungen und OCR-Gleichungen mit Seitenverweis;
- Bibliografie, DOI und lokale Dateipfade;
- Abbildungen in einem Pop-over mit Seitenkontext und Bildunterschrift;
- eingebettetes PDF und direkter PDF-Link als Fallback.

Die vollständige Zusammenfassung ist standardmäßig eingeklappt. Formeln werden lokal durch MathJax gerendert.

## Validierung

```bash
python3 tests/validate_course.py
python3 tests/validate_models.py
python3 tests/runtime_smoke.py
python3 tests/validate_translations.py
python3 tests/validate_v012_features.py
```

Ergebnis der Release-Prüfung:

- 0 fehlende lokale Links oder Quellenpfade;
- 40/40 unabhängige numerische Modellprüfungen bestanden;
- 4/4 Runtime-Smoke-Tests der Modellseiten bestanden;
- JavaScript-Syntaxprüfung aller Hauptseiten und Bundles bestanden;
- 32 Papers und 748 eingebettete Quellentexte im Offline-Bundle bestätigt;
- alle 64 als deutsch bezeichneten Übersetzungs-/Zusammenfassungsdateien auf längere englische Passagen geprüft;
- v0.12-Regressionsprüfungen für Navigation, Graph, mobile Quellenansicht, lokale Mathematik und Übersetzungsmetadaten bestanden.

Eine echte pixelbasierte Browserprüfung ließ sich in der Erstellungsumgebung nicht zuverlässig automatisieren. Die statischen, strukturellen, numerischen und simulierten Runtime-Prüfungen sind reproduzierbar in `tests/` enthalten.

## Wichtige Dateien

- `index.html` — Übersicht, Systemkarte und Einstiegsmodelle
- `primer.html` — integrierte mathematische Grundlagen und Primer
- `prehistory.html` — klassische Grenzen und Theorieentwicklung
- `historical_core.html` — 15 Modelle von 1900 bis 1928
- `foundations_tests.html` — Deutungen und Tests 1935–1982
- `quantum_information.html` — Quanteninformation und Algorithmen
- `source_reader.html` — offlinefähige Primärquellenansicht
- `data/source_offline_bundle.js` — Quellenindex und 748 Textressourcen
- `tests/` — reproduzierbare Validierung
