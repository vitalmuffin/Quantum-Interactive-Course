# Heisenberg 1925: Quantentheoretische Umdeutung

> Qualitätsvermerk: Die im Projekt enthaltene Ausgangsdatei ist eine englische Übersetzung der ursprünglich deutschsprachigen Arbeit. Eine frühere automatische Verarbeitung hatte diese englische Fassung fälschlich als deutsche Übersetzung abgelegt. Die folgende deutsche Aufbereitung wurde deshalb fachlich neu erstellt; sie ist keine vollständige Satz-für-Satz-Übersetzung.

## Ausgangsproblem

Die ältere Quantentheorie verband klassische Elektronenbahnen mit zusätzlichen Quantisierungsregeln. Für das Wasserstoffatom lieferte sie wichtige Erfolge, bei komplizierteren Atomen, gekreuzten Feldern und zeitabhängigen Anregungen entstanden jedoch grundlegende Schwierigkeiten. Besonders problematisch war, dass die Theorie mit Größen arbeitete, die sich im atomaren Bereich prinzipiell nicht direkt beobachten ließen: etwa einer genau festgelegten Elektronenbahn als Funktion der Zeit.

Heisenbergs Leitidee lautet daher: Eine neue Mechanik soll nur Beziehungen zwischen prinzipiell beobachtbaren Größen verwenden. Beobachtbar sind insbesondere die Frequenzen und Intensitäten der Strahlung, die bei Übergängen zwischen stationären Zuständen emittiert oder absorbiert wird.

## Übergangsgrößen statt Bahnen

An die Stelle einer klassischen Größe wie $x(t)$ tritt kein einzelner zeitabhängiger Zahlenwert. Heisenberg ordnet jedem möglichen Übergang von einem Zustand $n$ in einen Zustand $m$ eine komplexe Übergangsamplitude $X_{nm}$ und eine Übergangsfrequenz $\nu_{nm}$ zu. Die Frequenzen gehorchen dem Ritzschen Kombinationsprinzip:

$$
\nu_{nk}=\nu_{nm}+\nu_{mk}.
$$

Die Indizes geben also nicht Koordinaten eines Raumpunkts an, sondern Anfangs- und Endzustände eines Übergangs. Eine physikalische Größe wird dadurch zu einer Tabelle von Übergangseinträgen.

## Die neue Multiplikationsregel

Der entscheidende Schritt entsteht bei der Frage, welche Größe dem klassischen Produkt $x(t)y(t)$ entsprechen soll. Damit die Übergangsfrequenzen korrekt kombiniert werden, muss über alle möglichen Zwischenzustände $k$ summiert werden:

$$
(XY)_{nm}=\sum_k X_{nk}Y_{km}.
$$

Dies ist die Multiplikationsregel für Matrizen. Im Allgemeinen hängt das Ergebnis von der Reihenfolge ab:

$$
XY\neq YX.
$$

Die Nichtkommutativität ist kein nachträglich eingeführtes Detail. Sie folgt unmittelbar daraus, dass zusammengesetzte Übergänge über geordnete Zwischenzustände laufen. Damit entsteht eine Mechanik, deren Grundgrößen nicht gewöhnliche Zahlen, sondern nichtkommutierende Tabellen beziehungsweise Operatoren sind.

## Anwendung auf den Oszillator

Heisenberg prüft die neue Rechenweise unter anderem am anharmonischen Oszillator. Er entwickelt Übergangsfrequenzen und -amplituden störungstheoretisch und zeigt, dass sich bekannte Korrespondenzbeziehungen im Grenzfall großer Quantenzahlen wiederfinden. Gleichzeitig erhält er eine konsistente Quantisierungsbedingung und die Struktur der Energieniveaus, ohne eine unbeobachtbare Bahn vorauszusetzen.

Die Arbeit enthält die Matrixschreibweise noch nicht in der später üblichen Form. Born und Jordan erkannten kurz darauf, dass Heisenbergs Übergangstabellen Matrizen sind und formulierten den Formalismus systematisch.

## Physikalische Bedeutung

Heisenberg verwirft nicht jede klassische Vorstellung. Klassische Bewegung bleibt als Näherung für große Quantenzahlen und geeignete Zustände erhalten. Aufgegeben wird jedoch die Annahme, eine exakte klassische Bahn müsse auch dann das Fundament der Theorie bilden, wenn sie weder gemessen noch konsistent berechnet werden kann.

Die Arbeit verändert damit drei Dinge zugleich:

1. **Zustandsbeschreibung:** Übergänge zwischen stationären Zuständen ersetzen mikroskopische Bahnen.
2. **Rechenregeln:** Produkte werden als geordnete Summen über Zwischenzustände berechnet.
3. **Beobachtungsbezug:** Frequenzen und Intensitäten bilden den Ausgangspunkt der Theorie.

## Einordnung

Die Veröffentlichung gilt als Beginn der Matrixmechanik. Ihre wichtigste Leistung ist nicht nur eine neue Formel, sondern eine neue Auswahl der grundlegenden Größen. Aus dieser Auswahl folgen die nichtkommutative Algebra, später die Kommutatorrelationen und schließlich die moderne Operatorform der Quantenmechanik.
