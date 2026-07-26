# Modell- und Integritätsprüfung v0.10

## Ergebnis

- **40/40 unabhängige numerische Modellprüfungen bestanden**
- **4/4 simulierte Runtime-Smoke-Tests bestanden**
- **0 strukturelle oder lokale Verweisfehler**
- **32 Papers und 748 Quellentexte im Offline-Bundle vorhanden**

## Unabhängig geprüfte Modellbeziehungen

### Primer

Wellenbeziehung, konstruktive und destruktive Superposition, Gauß-Normierung, komplexe Norm, Basiswahrscheinlichkeiten, numerische Ableitung und Eigenwertskalierung.

### Historischer Kern

Planck-Maximum gegen Wiensches Verschiebungsgesetz, Photoeffekt-Schwelle, Balmer-Übergang, Einstein-Raten, maximale Compton-Verschiebung, de-Broglie-Wellenlänge, Quantenstatistik, Matrixunitarität, Kastennormierung, harmonischer Oszillator, Born-Normierung, Unschärfeprodukt, Molekülbindung einschließlich Kernabstoßung und Isotopeneffekt, Feldoszillator und Dirac-Dispersion.

### Grundlagen und Tests

EPR-Wahrscheinlichkeiten, reduzierte Dichtematrix, Bohmsche stationäre Geschwindigkeit, Everett-Basisgewichte, lokale Bell-Grenze, Tsirelson-Wert der CHSH-Einstellung, Kochen–Specker-Parität, Aspect-Lichtlaufzeit und Dekohärenz-Komplementarität.

### Quanteninformation

Zustandsraumspeicher, Bloch-Wahrscheinlichkeiten, unitäre Gatter, Verschränkungswahrscheinlichkeiten, No-Cloning-Überlappung, Teleportationsfidelität, BB84-QBER, Deutsch–Jozsa und Shor-Periodensuche.

## Runtime-Smoke-Test

Die Inline-Logik von `primer.html`, `historical_core.html`, `foundations_tests.html` und `quantum_information.html` wurde in einer simulierten DOM-Umgebung initialisiert und die jeweiligen Render-Einstiegspunkte wurden ausgeführt.

## Einschränkung

Die Build-Umgebung erlaubte keine zuverlässige automatisierte pixelbasierte Browserprüfung. Layout und Interaktion wurden deshalb zusätzlich über DOM-Struktur, lokale Ressourcen, JavaScript-Syntax, Modellinvarianten und simulierte Laufzeitpfade geprüft.
