# Übersetzungsprüfung v0.12

## Umfang

Geprüft wurden alle 32 Dateien `summaries/*/summary_german.md` sowie alle 32 Dateien `sources/*/text_german.md`. Die Prüfung kombiniert deutsche und englische Funktionswortquoten mit einer Satzprüfung auf längere englische Passagen.

## Gefundene Fehlklassifikationen

Drei Ordner enthielten in den als deutsch bezeichneten Dateien nahezu vollständig englischen Text:

- `09_1925_Heisenberg_Quantum_Reinterpretation_EN`
- `15_1926_Born_Collision_Processes_Probability_EN`
- `16_1927_Heisenberg_Physical_Content_Uncertainty_EN`

## Muster und Ursache

Alle drei Ordner enden auf `_EN`. Die eingebetteten Dokumente sind englische Übersetzungen ursprünglich deutschsprachiger Arbeiten. In den Metadaten war jedoch die Sprache des historischen Originals (`de`) zugleich als Sprache der tatsächlich eingebetteten Textfassung behandelt worden. Dadurch konnte die Übersetzungspipeline den englischen Eingangstext als bereits deutsch einstufen oder die falsche Sprachroute wählen. Das Problem ist daher eine Verwechslung von **Originalsprache des Werkes** und **Sprache der verwendeten Quelldatei**, nicht ein allgemeines zufälliges Azure-Übersetzungsproblem.

## Korrektur

- Die drei deutschen Zusammenfassungen wurden durch fachlich geprüfte deutsche Aufbereitungen ersetzt.
- Die fälschlich als deutscher Volltext bezeichneten Dateien enthalten nun dieselbe transparente deutsche Aufbereitung statt englischen Text.
- Die Metadaten unterscheiden jetzt `original_work_language: de` und `source_file_language: en`.
- `german_translation_available: false` verhindert, dass die Aufbereitung als vollständige Übersetzung ausgegeben wird.
- Die Quellenansicht weist bei diesen drei Arbeiten sichtbar auf die fehlende deutsche Volltextübersetzung hin.

## Ergebnis der Gesamtprüfung

Bei den übrigen 29 deutschen Zusammenfassungen und 29 deutschen Textfassungen wurden keine längeren englischen Passagen nach dem verwendeten Schwellenwert gefunden. Einzelne englische Fachbegriffe, Werktitel, Zitate und Variablennamen bleiben erwartungsgemäß erhalten.
