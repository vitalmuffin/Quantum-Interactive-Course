# Status v0.15

**Dauerhafte linke Etappenleiste mit Nummern und Auf-/Zuklappen:** umgesetzt  
**Etappenwechsel ohne Austausch der äußeren Kursoberfläche:** umgesetzt  
**Aktive Etappe wird live aktualisiert:** umgesetzt  
**Karussellpfeile an den Grenzen deaktiviert:** umgesetzt  
**Systemgraph aktualisiert Detailansicht und markiert Auswahl:** umgesetzt  
**Graph- und Detailfeld auf großen Displays gleich hoch:** umgesetzt  
**Eigenständiges lokales MathJax 3 mit direkter SVG-Ausgabe für Desktop, Mobilgeräte und `file://`:** umgesetzt  
**Quellengleichungen bleiben nach dem Setzen sichtbar:** umgesetzt  
**Große dynamische Display-Gleichungen werden nach MathJax-Bereitschaft gesetzt und bei Bedarf erneut versucht:** umgesetzt  
**Mobile Etappenleiste als kleines Off-Canvas-Menü ohne dauerhaft belegte Inhaltsbreite:** umgesetzt  
**Sieben Grundlagenabbildungen:** umgesetzt  
**Meta-/Layoutformulierungen aus sichtbaren Konzepttexten entfernt:** umgesetzt  
**64 deutsche Übersetzungs-/Zusammenfassungsdateien geprüft:** bestanden  
**Drei `_EN`-Fehlklassifikationen korrigiert und transparent markiert:** umgesetzt  
**40/40 numerische Modellprüfungen:** bestanden  
**4/4 Runtime-Smoke-Tests:** bestanden  
**Lokale Links und Quellenpfade:** ohne Fehler geprüft  

Eine visuelle Browserautomatisierung war in der Build-Umgebung durch eine systemweite Browser-URL-Sperrrichtlinie nicht ausführbar. JavaScript-Syntax, DOM-Struktur, Dateiverweise, Übersetzungsqualität, numerische Modelle und simulierte Laufzeitpfade wurden automatisiert geprüft.


## v0.15

Dynamische Display-Gleichungen wurden auf einen robusten, wiederholbaren MathJax-SVG-Renderpfad umgestellt. Die falsche Argumentreihenfolge der Quellenansicht und veraltete Browser-Caches werden abgefangen.
