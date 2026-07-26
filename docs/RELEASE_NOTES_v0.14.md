# Release Notes v0.14

## Mobile Etappen-Navigation

- Die Etappenleiste belegt auf Smartphones im geschlossenen Zustand keinen festen horizontalen Platz mehr.
- Statt der permanenten Nummernspalte erscheint ein kleines Menü-Symbol unterhalb der Kopfleiste.
- Das Symbol öffnet dieselbe Etappenleiste als Off-Canvas-Panel über dem Kursinhalt.
- Ein abgedunkelter Hintergrund schließt die Leiste bei Berührung außerhalb des Panels.
- Nach der Auswahl einer Etappe wird das Panel automatisch geschlossen.
- Eingebettete Kursseiten und der Hauptinhalt nutzen auf kleinen Displays wieder die volle Breite.
- Die vertikalen Abstände der Etappeneinträge wurden vereinheitlicht.

## Formeldarstellung

- MathJax 2 wurde durch ein lokal gebündeltes, eigenständiges MathJax-3-SVG-Paket ersetzt.
- Das neue Paket lädt keine nachgelagerten Konfigurations- oder Schriftdateien und ist deshalb robuster bei `file://`, lokalen Webservern und mobilen Browsern.
- Dynamisch erzeugte Formeln werden direkt über `tex2svgPromise()` gesetzt, statt zunächst als sichtbarer LaTeX-Rohtext in das Dokument geschrieben zu werden.
- Die Quellenansicht verwendet denselben Renderer für Schlüsselgleichungen, Markdown-Formeln und nachgeladenen Inhalt.
- Wiederholtes Aktualisieren einer Darstellung rendert unveränderte Formeln nicht erneut.
- SVG-Formeln werden auf schmalen Bildschirmen zentriert und auf die verfügbare Breite begrenzt.

## Paketstruktur

Die in v0.13 eingeführte Struktur bleibt erhalten. Die alte, nicht mehr verwendete MathJax-2-Verzeichnisstruktur wurde entfernt und durch `vendor/mathjax-tex-svg-full.js` ersetzt.
