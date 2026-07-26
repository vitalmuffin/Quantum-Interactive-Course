# Release Notes v0.12

## Navigation und Layout

- Eine dauerhaft sichtbare linke Etappenleiste zeigt im schmalen Zustand nur die Abschnittsnummern und kann über einen Schalter aufgeklappt werden.
- Beim Wechsel der Etappe bleibt die äußere Kursoberfläche bestehen; der Inhaltsbereich wird in einer eingebetteten Ansicht aktualisiert.
- Die aktive Etappe wird beim Seitenwechsel und beim Scrollen innerhalb der historischen Unteretappen unmittelbar aktualisiert.
- Die Pfeile des historischen Karussells werden am Anfang beziehungsweise Ende deaktiviert und ausgegraut.
- Systemgraph und Detailansicht besitzen auf großen Bildschirmen dieselbe Höhe. Ein Klick auf einen Graphknoten aktualisiert die Detailansicht und markiert den gewählten Knoten.

## Mathematik und Grundlagen

- MathJax wird lokal mit SVG-Ausgabe geladen; dadurch hängen Formeln auf Mobilgeräten nicht mehr von einem externen CDN ab.
- Die Gleichungen in der Quellenansicht werden über stabile MathJax-Skriptknoten aufgebaut und bleiben nach dem Rendern sichtbar.
- Formeln und zugehörige Inhalte sind zentriert und gegen horizontales Überlaufen abgesichert.
- Meta- und Layoutsätze wie „Warum hier wichtig …“ oder Hinweise zur Position der Formelzeichen wurden aus den sichtbaren Erklärungen entfernt.
- Die sieben Grundlagenblöcke enthalten kompakte SVG-Abbildungen: Sinus/Kosinus/Tangens, Funktionsaddition, Wahrscheinlichkeitsfläche, komplexe Ebene, Projektionen, Ableitung/Integral und Eigenrichtungen.

## Übersetzungsprüfung

- Alle deutschen Zusammenfassungen und deutschen Textfassungen wurden mit einer Sprachheuristik auf längere englische Passagen geprüft.
- Drei falsch klassifizierte `_EN`-Ordner wurden gefunden: Heisenberg 1925, Born 1926 und Heisenberg 1927.
- Ursache war die Verwechslung der historischen Originalsprache des Werkes mit der Sprache der tatsächlich eingebetteten Quelldatei.
- Die drei deutschen Dateien wurden durch geprüfte deutsche Aufbereitungen ersetzt. Die Metadaten unterscheiden nun `original_work_language` und `source_file_language` und kennzeichnen transparent, dass keine vollständige deutsche Übersetzung vorliegt.

## Mobile Ansicht

- Die linke Etappenleiste, der Fortschrittszugang und die Quellenetappe bleiben auf kleinen Bildschirmen erreichbar.
- Die Reiter der Quellenansicht sind horizontal scrollbar und bleiben beim Lesen sichtbar.
- Gleichungen, Quellkarten und Dateipfade brechen auf kleinen Displays kontrolliert um.
