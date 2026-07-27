# Wichtigste noch fehlende Prinzipien und Papers

Diese Liste ist bewusst kurz. Sie priorisiert Lücken, die mehrere spätere Themen zugleich verbessern. Die Papers sollten zunächst heruntergeladen, auf Nutzungsrechte geprüft, extrahiert, übersetzt und durch den bestehenden Quellenprozess geführt werden.

## Priorität 0 — als Nächstes ergänzen

### 1. Spin, Richtungsquantelung und Messbasis

**Warum es fehlt:** Spin erscheint im jetzigen Kurs vor allem indirekt über Pauli, Dirac und Qubits. Es fehlt die anschauliche Brücke von einer Messachse zu diskreten Ergebnissen sowie zu nichtkommutierenden aufeinanderfolgenden Messungen.

**Primärquellen:**

1. Walther Gerlach; Otto Stern (1922): *Der experimentelle Nachweis der Richtungsquantelung im Magnetfeld*. Zeitschrift für Physik 9, 349–352. DOI: `10.1007/BF01326983`.
2. Wolfgang Pauli (1927): *Zur Quantenmechanik des magnetischen Elektrons*. Zeitschrift für Physik 43, 601–623. DOI: `10.1007/BF01397326`.

**Kleinste sinnvolle Kurseinheit:** Stern–Gerlach-Aufbau, Wahl der Messachse, zwei mögliche Ausgänge, hintereinandergeschaltete Analysatoren, Pauli-Matrizen und Übergang zur Bloch-Kugel.

### 2. Direkter experimenteller Nachweis der Materiewellen

**Warum es fehlt:** de Broglies theoretischer Schritt ist enthalten, aber die historische Kette besitzt noch keinen eigenen zentralen Primärtext zur Elektronenbeugung. Dadurch ist die Trennung zwischen theoretischer Vorhersage und experimenteller Stützung an dieser Stelle schwächer als bei Photoeffekt oder Bell-Test.

**Primärquelle:**

Clinton Davisson; Lester H. Germer (1927): *Diffraction of Electrons by a Crystal of Nickel*. Physical Review 30, 705–740. DOI: `10.1103/PhysRev.30.705`.

**Kleinste sinnvolle Kurseinheit:** Elektronenenergie → de-Broglie-Wellenlänge → Bragg-Bedingung → erwarteter Winkel → gemessene Intensitätsmaxima.

### 3. Quantentunneln und Barrieren

**Warum es fehlt:** Tunneln ist eines der wichtigsten Beispiele dafür, dass die Wellenfunktion nicht wie eine klassische Teilchenbahn behandelt werden darf. Es verbindet Grundlagen, Kernphysik, Chemie und moderne Mikroskopie.

**Primärquelle:**

George Gamow (1928): *Zur Quantentheorie des Atomkernes*. Zeitschrift für Physik 51, 204–212. DOI: `10.1007/BF01343196`.

**Kleinste sinnvolle Kurseinheit:** endliche Barriere, exponentieller Abfall, Transmissionswahrscheinlichkeit, Abhängigkeit von Masse, Barrierenhöhe und -breite; Anwendung auf Alpha-Zerfall. Chemische Anwendungen können als spätere Vertiefung folgen.

## Priorität 1 — danach ergänzen

### 4. Dichteoperator, gemischte Zustände und Teilsysteme

**Warum es fehlt:** Der Kurs nutzt reduzierte Zustände, Dekohärenz und verrauschte Qubits, ohne den Dichteoperator früh genug als gemeinsames Werkzeug aufzubauen. Der Unterschied zwischen kohärenter Superposition und statistischem Gemisch sollte explizit werden.

**Primärquelle:**

John von Neumann (1927): *Wahrscheinlichkeitstheoretischer Aufbau der Quantenmechanik*. Nachrichten von der Gesellschaft der Wissenschaften zu Göttingen, Mathematisch-Physikalische Klasse, 245–272. Digitalisat: EuDML-Dokument 59230.

**Kleinste sinnvolle Kurseinheit:** `ρ = |ψ⟩⟨ψ|`, Gemisch, Reinheit `Tr(ρ²)`, partielle Spur und gleiche lokale Statistiken trotz verschiedener Gesamtzustände.

### 5. Dekohärenz und klassisch erscheinende Zustände

**Warum es fehlt:** Dekohärenz ist bereits als Modell vorhanden, aber ihr historischer und konzeptioneller Ursprung ist nicht als eigene Primärquelle eingebettet. Die Einheit sollte außerdem klar zwischen Unterdrückung lokaler Interferenz und einer Interpretation des Messergebnisses unterscheiden.

**Primärquelle:**

H. Dieter Zeh (1970): *On the Interpretation of Measurement in Quantum Theory*. Foundations of Physics 1, 69–76. DOI: `10.1007/BF00708656`.

**Kleinste sinnvolle Kurseinheit:** System–Umwelt-Verschränkung, reduzierte Dichtematrix, abklingende Off-Diagonalelemente, bevorzugte Zustände und die Aussagegrenze „Dekohärenz ist nicht automatisch ein ausgewähltes Einzelergebnis“.

## Noch keine neuen Downloads erforderlich

Zwei wichtige Vertiefungen können zunächst mit bereits vorhandenen Quellen gebaut werden:

- **Dreidimensionale Wellenmechanik, Drehimpuls und Orbitale:** Erweiterung der vorhandenen Schrödinger-Papers um Wasserstoff, Quantenzahlen, radiale und Winkelknoten sowie Orbitaldarstellungen.
- **Näherungsverfahren:** Born–Oppenheimer ist bereits enthalten. Variationsprinzip, Störungstheorie und Basisabschneidung sollten erst nach den fünf Prioritäten systematisch ergänzt werden, damit der Kurs nicht zu früh zu breit wird.

## Empfohlene Reihenfolge

```text
Spin/Stern–Gerlach
→ Davisson–Germer
→ Tunneln
→ Dichteoperator
→ Dekohärenz
```

Diese Reihenfolge schließt zuerst die sichtbarsten experimentellen und intuitiven Lücken und ergänzt danach das gemeinsame mathematische Werkzeug für Messung, Verschränkung und Quanteninformation.
