# Verklebungsprüfung nach dem Garbenprinzip

## Einordnung

Die Kursplattform ist nicht von selbst eine mathematische Garbe. Für die Prüfung wurde sie als prägarbenartige Informationsarchitektur modelliert:

- **Grundraum:** der Begriffs- und Zeitgraph des Kurses;
- **offene Bereiche:** Module, Paperansichten und Lernpfade;
- **lokale Schnitte:** deutsche/englische Erklärungen, Gleichungen, Simulationen, Quellen und Glossarbegriffe eines Bereichs;
- **Restriktionen:** Übergabe derselben Begriffe, Notation und Quellenbezüge an kleinere Teilbereiche und Überlappungen.

## Kriterien

### 1. Identität der Restriktion
Ein Abschnitt, der auf sich selbst eingeschränkt wird, bleibt unverändert.

**Ergebnis:** erfüllt. Paper-IDs, Sprachvarianten und Quellenpfade bleiben stabil.

### 2. Komposition der Restriktionen
Die Einschränkung von Gesamtkarte → Modul → Paper stimmt mit Gesamtkarte → Paper überein.

**Ergebnis:** erfüllt für Navigation, Paper-IDs, PDFs, Summaries und Source-Reader. Die Daten werden über dieselben kanonischen Ordnernamen verklebt.

### 3. Lokalität / Separiertheit
Zwei globale Darstellungen, die auf jeder Überdeckung übereinstimmen, müssen gleich sein.

**Ergebnis:** weitgehend erfüllt. Deutsch und Englisch teilen Paper-ID, Jahr, Autor, Quellenpfad und Gleichungsobjekt. Interpretationen werden von experimentellen Aussagen getrennt. Korrigiert wurden zwei Überlappungsprobleme:

- Bell wurde nicht mehr verkürzt als bloße Annahme „vorgegebener Resultate“ dargestellt, sondern über lokale Faktorisierbarkeit präzisiert.
- Das Kontextualitätsraster wurde ausdrücklich als Mermin–Peres-Brücke und nicht als originaler Kochen–Specker-Beweis bezeichnet.

### 4. Existenz einer Verklebung
Kompatible lokale Inhalte müssen sich zu einer globalen Kursansicht zusammensetzen lassen.

**Ergebnis:** erfüllt. Timeline, Module, Paperreader und Fortschrittsansicht können aus denselben 32 Paperdatensätzen zusammengesetzt werden. Alle statischen lokalen Referenzen wurden auf Existenz geprüft.

### 5. Eindeutigkeit der Verklebung
Die kompatiblen lokalen Inhalte sollen genau eine globale Zuordnung ergeben.

**Ergebnis:** erfüllt auf der Datenebene durch eindeutige Paper-IDs. Nicht eindeutig sind bewusst die philosophischen Interpretationen; diese werden deshalb nicht zu einer angeblich einzigen globalen Ontologie verklebt, sondern als alternative Deutungen nebeneinander gezeigt.

## Verbleibende Grenzen

- Die 1.785 aus OCR extrahierten Gleichungen sind lokale Quellenschnitte, aber nicht einzeln fachlich verifiziert. Sie werden entsprechend gekennzeichnet.
- Der zitiergesicherte Zitatbestand bleibt leer, solange keine Passage seitenweise manuell bestätigt ist. Es werden keine Zitate erfunden.
- Einige Simulationen sind idealisierte Modelle. Ihre lokale Gültigkeit wird benannt; sie dürfen nicht ohne diese Einschränkung auf reale Apparate verklebt werden.

## Gesamturteil

Die Plattform erfüllt die Garbenanalogie auf Ebene von Identität, Restriktionskomposition, lokaler Konsistenz und eindeutiger Datenverklebung. Die wichtigsten Hindernisse lagen nicht in fehlenden Dateien, sondern in semantisch inkompatiblen Überlappungen. Diese wurden in v0.8 korrigiert oder explizit als Modellgrenzen markiert.
