# Roadmap: Interaktiver Webkurs zur Entwicklung der Quantenmechanik

Version: 1.0  
Arbeitsmodus: Etappen mit klaren Abnahmekriterien  
Sprachen: Deutsch und Englisch  
Primärquellen: 32 historische Papers mit Originaltext, Übersetzungen, Zusammenfassungen, Bildern und PDFs

---

## 1. Zielbild

Der Kurs soll die Entwicklung der Quantenmechanik als zusammenhängendes System zeigen:

**Beobachtung → Krise des bisherigen Modells → neue Annahme → Formalismus → Vorhersage → Experiment → Veränderung des Weltbilds**

Die Lernenden sollen:

- ohne vorausgesetzte Hochschulmathematik einsteigen können;
- zuerst eine intuitive Vorstellung aufbauen;
- danach denselben Inhalt formal mit Gleichungen sehen;
- historische Experimente interaktiv verändern können;
- verstehen, welche Theorie durch welche Beobachtung gestützt oder widerlegt wurde;
- erkennen, wie einzelne Ideen voneinander abhängen;
- jederzeit zur Primärquelle, Zusammenfassung, Abbildung oder Originalgleichung springen können;
- zwischen Deutsch und Englisch wechseln können.

---

# 2. Gesamtstruktur des Projekts

## Phase A — Quellen und Datenmodell

### A1. Quellenbestand prüfen

- [ ] Alle 32 Paper-Ordner erfassen
- [ ] Vorhandene Dateien je Paper prüfen:
  - [ ] `markdown.md`
  - [ ] `text_german.md`
  - [ ] `text_english.md`
  - [ ] `summary_german.md`
  - [ ] `summary_english.md`
  - [ ] `document-annotation.json`
  - [ ] `pages/`
  - [ ] PDF-Datei
- [ ] Fehlende oder anders benannte Dateien dokumentieren
- [ ] Einheitliche Paper-ID festlegen
- [ ] Chronologische Reihenfolge final bestätigen

**Ergebnis:** `papers_index.json`

### A2. Einheitliches Datenmodell definieren

Jedes Paper erhält mindestens:

```json
{
  "id": "03_1913_Bohr_Constitution_Atoms_Part_I",
  "year": 1913,
  "authors": ["Niels Bohr"],
  "title_de": "...",
  "title_en": "...",
  "original_language": "en",
  "summary_de": "...",
  "summary_en": "...",
  "key_questions": [],
  "old_model": "",
  "new_assumption": "",
  "key_equations": [],
  "experiments": [],
  "images": [],
  "quotes": [],
  "disproved_or_limited": [],
  "enabled": true
}
```

- [ ] JSON-Schema erstellen
- [ ] Parser für bestehende Markdown-Dateien erstellen
- [ ] automatische Pfadprüfung einbauen
- [ ] Datenvalidierung integrieren

**Abnahmekriterium:** Alle 32 Papers lassen sich ohne Sonderfälle als strukturierte Datensätze laden.

---

## Phase B — Didaktisches Grundgerüst

### B1. Lernpfade festlegen

Drei parallele Ebenen:

1. **Intuition**
   - Bilder
   - Animationen
   - Analogien
   - Experimente
   - wenig Text

2. **Historische Entwicklung**
   - Was war bekannt?
   - Was passte nicht?
   - Welche Idee wurde eingeführt?
   - Was wurde dadurch erklärbar?
   - Was blieb offen?

3. **Formalismus**
   - Gleichungen
   - Variablen
   - Rechenbeispiele
   - Grenzen der Modelle

- [ ] Ebene je Abschnitt sichtbar umschaltbar machen
- [ ] Fortschritt unabhängig je Ebene speichern
- [ ] Begriffe automatisch verlinken

### B2. Mathematische Voraussetzungen

Module vor dem historischen Kern:

- [ ] Größen, Einheiten und Größenordnungen
- [ ] Funktionen und Graphen
- [ ] Wellenlänge, Frequenz, Phase
- [ ] Summen und Überlagerung
- [ ] Wahrscheinlichkeit
- [ ] Mittelwert und Erwartungswert
- [ ] Vektoren
- [ ] komplexe Zahlen als rotierende Pfeile
- [ ] Ableitung als lokale Änderungsrate
- [ ] Integral als aufsummierte Fläche
- [ ] Eigenwert und Eigenzustand intuitiv

**Abnahmekriterium:** Eine Person mit Realschulabschluss kann die späteren Visualisierungen bedienen und die verwendeten Symbole zuordnen.

---

## Phase C — Visuelles und technisches Fundament

### C1. Technologiestack

- [ ] HTML5
- [ ] CSS mit Design-Tokens
- [ ] Vanilla JavaScript oder klar begründetes Framework
- [ ] Temml für LaTeX
- [ ] Plotly für Diagramme
- [ ] Canvas für Simulationen
- [ ] Viz.js oder Graphviz-WASM für Abhängigkeitsgraphen
- [ ] Markdown-Renderer
- [ ] PDF.js für PDFs
- [ ] lokale JSON-Daten
- [ ] keine zwingende Serverabhängigkeit für die Offline-Version

### C2. Designsystem

- [ ] Farbsystem für:
  - Beobachtung
  - Theorie
  - Experiment
  - Widerlegung
  - offene Frage
- [ ] Typografie
- [ ] Karten
- [ ] Timeline-Elemente
- [ ] Gleichungsblöcke
- [ ] Slider und Eingabefelder
- [ ] Diagrammlegenden
- [ ] Hinweis- und Warnkomponenten
- [ ] mobile Darstellung
- [ ] Dark Mode
- [ ] barrierefreie Kontraste

### C3. Grundlayout

- [ ] Startseite mit abstraktem Systemmuster
- [ ] interaktive Gesamttimeline
- [ ] Systemgraph der Abhängigkeiten
- [ ] Modulnavigation
- [ ] Paper-Detailseite
- [ ] Experimentansicht
- [ ] Glossar
- [ ] Quellenansicht
- [ ] Sprachumschalter DE/EN

**Abnahmekriterium:** Die Plattform ist als leere, aber vollständige Kursschale navigierbar.

---

# 3. Inhaltliche Hauptmodule

## Modul 0 — Wie Wissenschaft Modelle verändert

Kernmuster:

- Beobachtung
- Erklärung
- Vorhersage
- Messung
- Konflikt
- neues Modell
- Gültigkeitsbereich

Interaktionen:

- [ ] Modellvergleich
- [ ] Unsicherheit von Messungen
- [ ] Theorie kann erfolgreich und trotzdem unvollständig sein
- [ ] klassische Physik als Grenzfall der Quantenphysik

---

## Modul 1 — Strahlung wird quantisiert

Historische Achse:

- Kirchhoff
- Wien
- Rayleigh
- Planck
- Einstein
- Debye
- Einstein 1917

Interaktionen:

- [ ] Schwarzkörperstrahlung:
  - Temperatur
  - Wellenlänge
  - Wien-Gesetz
  - Rayleigh-Jeans-Gesetz
  - Planck-Verteilung
- [ ] Ultraviolettkatastrophe
- [ ] Photoeffekt:
  - Lichtfrequenz
  - Intensität
  - Austrittsarbeit
  - Elektronenenergie
- [ ] Photonenergie
- [ ] spontane und stimulierte Emission

Zentrale Gleichungen:

\[
\underbrace{E}_{\text{Photonenergie}}
=
\underbrace{h}_{\text{Planck-Konstante}}
\underbrace{\nu}_{\text{Frequenz}}
\]

\[
\underbrace{K_\mathrm{max}}_{\text{maximale Elektronenenergie}}
=
\underbrace{h\nu}_{\text{Photonenergie}}
-
\underbrace{\Phi}_{\text{Austrittsarbeit}}
\]

**Abnahmekriterium:** Die Lernenden können erklären, warum Intensität und Frequenz beim Photoeffekt verschiedene Rollen spielen.

---

## Modul 2 — Das Atom bekommt diskrete Zustände

Historische Achse:

- Rutherford
- Bohr
- Sommerfeld
- Stark-Effekt
- Zeeman-Effekt
- Spektrallinien

Interaktionen:

- [ ] Rutherford-Streuversuch
- [ ] Bohr-Radien
- [ ] Energieniveaus
- [ ] Wasserstoffspektrum
- [ ] Übergänge per Drag-and-drop
- [ ] Emissions- und Absorptionslinien
- [ ] Einfluss äußerer Felder

Zentrale Gleichungen:

\[
\underbrace{E_n}_{\text{Energie des Zustands}}
=
-\frac{
\underbrace{13.6\,\mathrm{eV}}_{\text{Grundenergie des Wasserstoffatoms}}
}{
\underbrace{n^2}_{\text{Quantenzahl}}
}
\]

\[
\underbrace{\Delta E}_{\text{Energieunterschied}}
=
\underbrace{h\nu}_{\text{Energie des emittierten oder absorbierten Photons}}
\]

**Abnahmekriterium:** Die Lernenden können aus einem Übergang zwischen zwei Energieniveaus eine Photonfrequenz bestimmen.

---

## Modul 3 — Licht und Materie zeigen Wellen- und Teilchenverhalten

Historische Achse:

- Compton
- de Broglie
- Davisson-Germer
- Doppelspalt
- Materiewellen

Interaktionen:

- [ ] Compton-Streuung:
  - Streuwinkel
  - Photonenenergie
  - Elektronenrückstoß
- [ ] de-Broglie-Wellenlänge
- [ ] Doppelspalt:
  - Teilchengröße
  - Masse
  - Geschwindigkeit
  - Spaltabstand
  - Spaltbreite
  - Dekohärenz
- [ ] klassischer Grenzfall
- [ ] Einzeltreffer bauen Interferenzmuster auf

Zentrale Gleichung:

\[
\underbrace{\lambda}_{\text{Materiewellenlänge}}
=
\frac{
\underbrace{h}_{\text{Planck-Konstante}}
}{
\underbrace{p}_{\text{Impuls}}
}
\]

**Abnahmekriterium:** Die Lernenden erkennen, dass nicht „entweder Welle oder Teilchen“, sondern der Versuchsaufbau die beobachtbaren Eigenschaften bestimmt.

---

## Modul 4 — Die neue Mechanik entsteht

Historische Achse:

- Heisenberg
- Born
- Jordan
- Dirac
- Schrödinger
- Born-Regel

Interaktionen:

- [ ] Zustände als Vektoren
- [ ] Operatoren als Aktionen
- [ ] Matrizenmultiplikation visuell
- [ ] Wellenfunktion
- [ ] Eigenzustände
- [ ] Wahrscheinlichkeitsdichte
- [ ] Vergleich Matrixmechanik und Wellenmechanik
- [ ] Wellenpaket aus Einzelwellen zusammensetzen

Zentrale Gleichungen:

\[
\underbrace{i\hbar\frac{\partial}{\partial t}\psi}_{\text{zeitliche Änderung des Zustands}}
=
\underbrace{\hat H\psi}_{\text{Energieoperator auf dem Zustand}}
\]

\[
\underbrace{P(x)}_{\text{Wahrscheinlichkeit}}
=
\underbrace{|\psi(x)|^2}_{\text{Betragsquadrat der Wellenfunktion}}
\]

**Abnahmekriterium:** Die Lernenden können Wellenfunktion und Wahrscheinlichkeit unterscheiden.

---

## Modul 5 — Unschärfe, Messung und Komplementarität

Historische Achse:

- Heisenberg
- Bohr
- Pauli
- Stern-Gerlach
- Spin

Interaktionen:

- [ ] Wellenpaket und Impulsverteilung
- [ ] Fourier-Intuition
- [ ] Stern-Gerlach:
  - Magnetfeldgradient
  - Teilchengeschwindigkeit
  - Spinpräparation
  - Geräteorientierung
  - mehrstufige Apparaturen
- [ ] Messbasis
- [ ] nichtkommutierende Beobachtungen

Zentrale Gleichung:

\[
\underbrace{\Delta x}_{\text{Ortsunschärfe}}
\underbrace{\Delta p}_{\text{Impulsunschärfe}}
\ge
\frac{
\underbrace{\hbar}_{\text{reduzierte Planck-Konstante}}
}{2}
\]

**Abnahmekriterium:** Die Lernenden verstehen, dass die Unschärferelation keine bloße Messgeräteungenauigkeit beschreibt.

---

## Modul 6 — Viele identische Teilchen

Historische Achse:

- Bose
- Einstein
- Pauli
- Fermi
- Dirac

Interaktionen:

- [ ] Bosonen vs. Fermionen
- [ ] Besetzungszahlen
- [ ] Pauli-Prinzip
- [ ] Fermi-See
- [ ] Bose-Einstein-Kondensation
- [ ] Temperaturabhängigkeit

**Abnahmekriterium:** Die Lernenden können erklären, warum Materiestruktur und Laserlicht unterschiedliche Statistik verwenden.

---

## Modul 7 — Moleküle und Quantenchemie

Historische Achse:

- Heitler-London
- Born-Oppenheimer
- Molekülbindung

Interaktionen:

- [ ] zwei Wasserstoffatome annähern
- [ ] bindende und antibindende Zustände
- [ ] Elektronendichte
- [ ] Kernbewegung vs. Elektronenbewegung
- [ ] Potentialkurven
- [ ] Schwingungsniveaus

**Abnahmekriterium:** Die Lernenden verstehen, warum die Born-Oppenheimer-Näherung Molekülrechnungen ermöglicht.

---

## Modul 8 — Relativistische Quantenmechanik und Felder

Historische Achse:

- Klein
- Dirac
- Fockraum
- Antimaterie
- QED
- Feynman
- Dyson
- Tomonaga

Interaktionen:

- [ ] Dirac-Energiespektrum
- [ ] Klein-Paradoxon
- [ ] Teilchenerzeugung und -vernichtung
- [ ] Feynman-Diagramme als Rechenorganisation
- [ ] Pfadintegral-Intuition

**Abnahmekriterium:** Die Lernenden erkennen, warum relativistische Quantenphysik eine Feldtheorie verlangt.

---

## Modul 9 — Was bedeutet die Theorie?

Historische Achse:

- EPR
- Schrödinger
- Bohm
- Everett
- von Neumann
- Birkhoff
- Gleason

Systemische Fragen:

- Ist die Wellenfunktion vollständig?
- Ist Zufall fundamental?
- Hat ein Messergebnis vor der Messung einen festen Wert?
- Welche Rolle spielt der Beobachter?
- Was bedeutet „Realität“ in einer physikalischen Theorie?

Interaktionen:

- [ ] verschränkte Zustände
- [ ] EPR-Szenario
- [ ] Bohmsche Trajektorien
- [ ] Viele-Welten-Verzweigung als Interpretationsdiagramm
- [ ] Messproblem als Prozessgraph

**Abnahmekriterium:** Interpretationen werden getrennt von experimentell bestätigten Vorhersagen dargestellt.

---

## Modul 10 — Bell, Kontextualität und experimentelle Tests

Historische Achse:

- Bell
- CHSH
- Kochen-Specker
- Aspect

Interaktionen:

- [ ] lokale verborgene Variablen simulieren
- [ ] Quantenkorrelation simulieren
- [ ] Detektoreinstellungen verändern
- [ ] CHSH-Wert berechnen
- [ ] statistische Unsicherheit
- [ ] Schlupflöcher historisch einordnen

Zentrale Gleichung:

\[
\underbrace{|S|}_{\text{CHSH-Kombination}}
\le
\underbrace{2}_{\text{Grenze lokaler realistischer Modelle}}
\]

Quantenmechanik erlaubt bis:

\[
|S| \le 2\sqrt{2}
\]

**Abnahmekriterium:** Die Lernenden können präzise sagen, was Bell-Experimente ausschließen und was sie nicht ausschließen.

---

## Modul 11 — Dekohärenz und klassischer Grenzfall

Historische Achse:

- Zeh
- offene Quantensysteme
- Umwelteinfluss

Interaktionen:

- [ ] System koppelt an Umgebung
- [ ] Interferenzkontrast nimmt ab
- [ ] Dichtematrix
- [ ] reduzierte Dichtematrix
- [ ] klassische Erscheinung großer Systeme

**Abnahmekriterium:** Die Lernenden unterscheiden Dekohärenz vom eigentlichen Messproblem.

---

## Modul 12 — Quanteninformation und Quantencomputer

Historische Achse:

- Landauer
- Bennett
- Holevo
- Feynman
- No-Cloning
- BB84
- Deutsch
- Shor

Interaktionen:

- [ ] Qubit auf Bloch-Kugel
- [ ] Einzel- und Zwei-Qubit-Gatter
- [ ] Interferenz im Algorithmus
- [ ] No-Cloning
- [ ] Quantenteleportation
- [ ] BB84
- [ ] Deutsch-Jozsa
- [ ] Shor als Prozesskette:
  - Periodenfindung
  - Quanten-Fourier-Transformation
  - klassisches Nachrechnen

**Abnahmekriterium:** Die Lernenden verstehen, dass Quantencomputer nicht einfach „alle Lösungen gleichzeitig ausprobieren und auslesen“.

---

# 4. Komponenten, die mehrfach verwendet werden

## 4.1 Gleichungs-Komponente

- [ ] Temml-Rendering
- [ ] Underbraces zur Variablenerklärung
- [ ] Einheitenanzeige
- [ ] Werte per Slider einsetzen
- [ ] Zwischenschritte ein- und ausblenden
- [ ] numerisches Ergebnis
- [ ] Grenzfälle
- [ ] Verlinkung zur Primärquelle

## 4.2 Experiment-Komponente

Jedes Experiment besitzt:

- historische Fragestellung
- Aufbau
- einstellbare Parameter
- beobachtbare Größe
- Modellvergleich
- Messrauschen
- Vorhersage
- tatsächlich beobachtetes Ergebnis
- historische Konsequenz
- Grenzen der Aussage

## 4.3 Quellen-Komponente

- Summary oben
- Primärquellenbild
- relevante Gleichung
- Zitat
- Seitenangabe
- PDF-Viewer
- Sprungmarke zur Stelle im PDF
- deutsche und englische Fassung
- klare Kennzeichnung:
  - Original
  - Übersetzung
  - moderne Erklärung
  - Interpretation

## 4.4 Glossar-Komponente

- einfache Definition
- formale Definition
- visuelles Beispiel
- verwandte Begriffe
- erste historische Verwendung im Kurs
- typische Missverständnisse

---

# 5. Zitate und Zitiersicherheit

## Regeln

- [ ] Nur Zitate verwenden, die in einer Primärquelle oder verlässlichen Edition überprüft wurden
- [ ] keine populären Fehlzitate
- [ ] Originalsprache speichern
- [ ] Übersetzung separat kennzeichnen
- [ ] Seitenzahl oder Abschnitt angeben
- [ ] Klick auf Zitat öffnet PDF an der relevanten Stelle
- [ ] unsichere Zitate nicht verwenden

## Datenstruktur

```json
{
  "quote_original": "...",
  "quote_de": "...",
  "quote_en": "...",
  "author": "...",
  "paper_id": "...",
  "page": 12,
  "verified": true
}
```

---

# 6. Reihenfolge der Umsetzung

## Sprint 1 — Fundament

- [ ] Repositorystruktur erstellen
- [ ] 32 Paper in ein Datenmodell überführen
- [ ] Sprachumschaltung
- [ ] Designsystem
- [ ] Temml integrieren
- [ ] Plotly integrieren
- [ ] PDF.js integrieren
- [ ] erste Systemkarte
- [ ] erste Timeline

**Definition of Done:** Alle 32 Papers erscheinen als anklickbare Knoten mit Jahr, Titel und Kurzthese.

## Sprint 2 — Abstrakte Systemmuster

- [ ] Wissenschaftszyklus visualisieren
- [ ] Theorieabhängigkeiten zeigen
- [ ] klassische vs. quantenmechanische Denkweise
- [ ] Grenzen und Gültigkeitsbereiche
- [ ] philosophische Prämissen als Karten

**Definition of Done:** Eine Person versteht die Gesamtstruktur, bevor einzelne Formeln erscheinen.

## Sprint 3 — Mathematischer Primer

- [ ] Wellen
- [ ] Frequenz
- [ ] Phase
- [ ] Superposition
- [ ] Wahrscheinlichkeit
- [ ] komplexe Zahlen
- [ ] Vektoren
- [ ] Operatoren

**Definition of Done:** Alle später benötigten Grundbegriffe sind interaktiv erfahrbar.

## Sprint 4 — Strahlung und frühe Quantentheorie

- [ ] Schwarzkörperstrahlung
- [ ] Photoeffekt
- [ ] Einstein-Koeffizienten
- [ ] Bohr-Atom
- [ ] Spektrallinien
- [ ] Compton-Effekt

## Sprint 5 — Materiewellen und neue Mechanik

- [ ] de Broglie
- [ ] Doppelspalt
- [ ] Matrixmechanik
- [ ] Schrödinger-Gleichung
- [ ] Born-Regel
- [ ] Wellenpakete

## Sprint 6 — Spin, Unschärfe und Statistik

- [ ] Stern-Gerlach
- [ ] Messbasis
- [ ] Unschärfe
- [ ] Bosonen
- [ ] Fermionen
- [ ] Pauli-Prinzip

## Sprint 7 — Moleküle, Relativität und Felder

- [ ] Heitler-London
- [ ] Born-Oppenheimer
- [ ] Dirac-Gleichung
- [ ] Antimaterie
- [ ] Pfadintegral
- [ ] QED

## Sprint 8 — Grundlagenstreit

- [ ] EPR
- [ ] Schrödinger
- [ ] Bohm
- [ ] Everett
- [ ] Messproblem
- [ ] Interpretationsvergleich

## Sprint 9 — Bell und experimentelle Tests

- [ ] Bell
- [ ] CHSH
- [ ] Kochen-Specker
- [ ] Aspect
- [ ] statistische Auswertung
- [ ] Aussagegrenzen

## Sprint 10 — Dekohärenz und Quanteninformation

- [ ] Dekohärenz
- [ ] Landauer
- [ ] No-Cloning
- [ ] BB84
- [ ] Teleportation
- [ ] Deutsch-Jozsa
- [ ] Shor

## Sprint 11 — Quellenintegration

- [ ] 32 PDFs einbinden
- [ ] Summaries über PDF anzeigen
- [ ] Originalbilder zuordnen
- [ ] Gleichungsreferenzen
- [ ] Zitate mit Seitenangabe
- [ ] moderne Vergleichsgrafiken

## Sprint 12 — Qualität und Veröffentlichung

- [ ] wissenschaftliche Prüfung
- [ ] Sprachprüfung Deutsch
- [ ] Sprachprüfung Englisch
- [ ] Barrierefreiheit
- [ ] Mobilgeräte
- [ ] Ladezeit
- [ ] Offline-ZIP
- [ ] Deployment-Dokumentation

---

# 7. Priorität der interaktiven Experimente

## Muss enthalten

1. Schwarzkörperstrahlung
2. Photoeffekt
3. Bohr-Energieniveaus
4. Compton-Streuung
5. Doppelspalt
6. Wellenpaket-Superposition
7. Stern-Gerlach
8. Unschärferelation
9. Bell/CHSH
10. Dekohärenz
11. Qubit und Gatter
12. Shor-Prozessübersicht

## Sollte enthalten

13. Rutherford-Streuung
14. Stark- und Zeeman-Aufspaltung
15. Bose- und Fermi-Verteilungen
16. Heitler-London-Bindung
17. Born-Oppenheimer-Potentialkurven
18. Klein-Paradoxon
19. Aharonov-Bohm-Effekt
20. Quanten-Teleportation

## Optional

21. Wigner-Funktion
22. Pfadintegral
23. Kochen-Specker-Kontextualität
24. Bohmsche Trajektorien
25. Viele-Welten-Verzweigungsdiagramm

---

# 8. Definition of Done für jedes Modul

Ein Modul ist abgeschlossen, wenn:

- [ ] deutsche und englische Texte vorhanden sind;
- [ ] historische Reihenfolge korrekt ist;
- [ ] mindestens eine Primärquelle eingebunden ist;
- [ ] wichtige Gleichungen mit Variablenerklärung vorhanden sind;
- [ ] mindestens eine interaktive Visualisierung vorhanden ist;
- [ ] eine einfache Erklärung vorhanden ist;
- [ ] eine formale Erklärung vorhanden ist;
- [ ] ein Beispiel gerechnet werden kann;
- [ ] Vorhersage und experimentelles Ergebnis getrennt dargestellt werden;
- [ ] klar genannt wird, was bestätigt, eingeschränkt oder widerlegt wurde;
- [ ] philosophische Interpretation nicht als experimentelle Tatsache dargestellt wird;
- [ ] alle Zitate überprüft sind;
- [ ] mobile und barrierefreie Bedienung geprüft ist.

---

# 9. Sofortiger nächster Arbeitsschritt

## Etappe 1: Systemkarte und visuelle Kursschale

Konkrete Aufgaben:

1. [ ] neue Projektstruktur anlegen
2. [ ] alle 32 Paper-IDs laden
3. [ ] `papers_index.json` erzeugen
4. [ ] Startseite bauen
5. [ ] abstrakten Wissenschaftszyklus visualisieren
6. [ ] chronologische Timeline rendern
7. [ ] Abhängigkeitsgraph rendern
8. [ ] Sprachumschaltung implementieren
9. [ ] Temml-Testgleichung einbauen
10. [ ] Plotly-Testdiagramm einbauen
11. [ ] Canvas-Testsimulation einbauen
12. [ ] PDF.js-Platzhalteransicht einbauen

**Ergebnis der nächsten Version:** `v0.2`

`v0.2` zeigt bereits das vollständige System der 32 Papers, obwohl die einzelnen Experimente noch nicht vollständig ausgebaut sind.
