# Modell- und Integritätsprüfung v0.9

## Ergebnis

- **39/39 unabhängige numerische Modellprüfungen bestanden**
- **4/4 Modellseiten im DOM-/Canvas-/Plotly-Runtime-Smoke-Test bestanden**
- **9 HTML-Dateien, 423 lokale Verweise und 32 Primärarbeiten geprüft**
- **0 fehlende lokale Dateien, 0 fehlende Anker, 0 unbekannte Paper-IDs**
- **JavaScript-Syntax aller HTML-Seiten und gemeinsam genutzten Skripte bestanden**
- **HTTP-Test der Hauptseiten, des Quellenindex und eines PDFs: Status 200**

## Geprüfte Modelle

### Grundlagen und Primer

1. Welle und Ausbreitungsgeschwindigkeit
2. konstruktive und destruktive Superposition
3. normierte Gauß-Wahrscheinlichkeitsdichte und 68,27-%-Intervall
4. komplexe Phase und Eulersche Darstellung
5. Basiswechsel und normierte Messwahrscheinlichkeiten
6. Ableitung und numerische Integration
7. Eigenvektoren und Eigenwerte

### Historischer Kern 1900–1928

1. Planck-Verteilung und Wien-Maximum
2. Photoeffekt und Grenzfrequenz
3. Bohr-Übergang 3 → 2
4. Einstein-Koeffizienten als normiertes Ratenmodell
5. maximale Compton-Verschiebung
6. de-Broglie-Wellenlänge eines Elektrons
7. Bose–Einstein-, Fermi–Dirac- und klassische Statistik
8. unitäre Matrixtransformation
9. Normierung und n²-Energieskalierung im Kasten
10. Born-Wahrscheinlichkeit
11. minimale Heisenberg-Unschärfe
12. bindender und antibindender Molekülzustand
13. harmonische Feldmoden
14. relativistische Dirac-Dispersion

### Grundlagen und Tests 1935–1982

1. EPR-Korrelation und normierte gemeinsame Wahrscheinlichkeiten
2. positive reduzierte Dichtematrix des Katzenmodells
3. Bohmsche Führungsgeschwindigkeit im stationären Grenzfall
4. normierte Everett-Zweiggewichte
5. lokale CHSH-Grenze durch vollständige Enumeration
6. quantenmechanisches CHSH-Maximum 2√2
7. Kochen–Specker-Paritätswiderspruch
8. Lichtlaufzeit im Aspect-Timingmodell
9. exponentielle Dekohärenz und Komplementaritätsrelation

### Quanteninformation

1. exponentielle Zustandsvektor-Speicherskalierung
2. Bloch-Kugel und Basiswahrscheinlichkeiten
3. Normerhaltung durch X- und Hadamard-Gatter
4. gemeinsame Wahrscheinlichkeiten eines Bell-Zustands
5. No-Cloning-Skalarproduktargument
6. Teleportationsfidelität des vereinfachten Werner-Kanals
7. erwartete BB84-Fehlerrate bei Intercept-Resend und Kanalrauschen
8. ideales Deutsch–Jozsa-Ergebnis
9. Shor-Beispiel N = 15, a = 2, Periode 4, Faktoren 3 und 5

## Behobene fachliche oder darstellerische Probleme

- Im Bose–Einstein-Modell konnte zuvor ein nicht zulässiges chemisches Potential oberhalb der Grundzustandsenergie gewählt werden. Für die dargestellte Skala gilt jetzt zwingend `μ < 0`.
- Die reine Planck-Ansicht nutzte zuvor teilweise den großen Wertebereich der Rayleigh–Jeans-Kurve und wirkte dadurch unnötig gestaucht. Die y-Skalierung wurde getrennt.
- Formeln wurden aus den schmalen Kontrollspalten entfernt und unter die Visualisierungen verschoben.
- Underbrace-Konstruktionen wurden in allen 32 historischen beziehungsweise experimentellen Modellen entfernt. Die Größen werden nun unter der Gleichung einzeln erklärt.
- Paper- und Aufbereitungslinks wurden an jedem experimentellen Informationsfeld ergänzt.

## Reproduzierbare Prüfungen

```bash
python3 tests/validate_course.py
python3 tests/validate_models.py
python3 tests/runtime_smoke.py
```

`validate_course.py` prüft Dateien, Links, Anker, Paper-IDs und die erwartete Seitenstruktur.  
`validate_models.py` führt die 39 unabhängigen numerischen Prüfungen aus.  
`runtime_smoke.py` lädt die JavaScript-Modelle in einer simulierten DOM-/Canvas-/Plotly-Umgebung und ruft alle Renderfunktionen auf.

## Grenze der Prüfung

Die Erstellungsumgebung blockierte einen echten grafischen Chromium-Lauf. Deshalb wurde kein automatisierter Pixelvergleich durchgeführt. Die Kombination aus Pfadprüfung, DOM-Strukturprüfung, JavaScript-Syntaxprüfung, Runtime-Smoke-Test, HTTP-Test und unabhängigen numerischen Invarianten deckt Funktions- und Rechenfehler ab, ersetzt aber keine abschließende manuelle Sichtprüfung in mehreren Browsern und Bildschirmgrößen.
