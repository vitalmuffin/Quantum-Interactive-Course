# Release Notes v0.13

## Navigation und Sidebar

- Das redundante **Etappen**-Steuerelement wurde aus der Kopfleiste entfernt.
- Die linke Etappenleiste verwendet feste 43-px-Zeilen und `align-content: start`; Einträge werden nicht mehr über die gesamte Höhe auseinandergezogen.
- Interne Etappenlinks werden auch aus eingebetteten Kursseiten an den äußeren Kursrahmen weitergereicht. Dadurch erzeugt **Geführten Kurs beginnen** keine zweite Kopfleiste oder Sidebar mehr.
- Etappenwechsel aktualisieren weiterhin nur den Inhalts-Frame; der äußere Kursrahmen bleibt bestehen.

## Mobiler Systemgraph

- SVG-Inhalte werden aus dem Template geklont, statt per `innerHTML` neu geparst zu werden. Das ist insbesondere in mobilen WebKit-Browsern robuster.
- Ein-Finger-Verschieben funktioniert nun auch, wenn die Geste auf einem Knoten beginnt.
- Zwei-Finger-Zoom, Mausrad-Zoom, Zoomtasten und Tastatursteuerung verwenden denselben Transformationszustand.
- Nach einer Zieh- oder Zoomgeste wird kein unbeabsichtigter Knotenklick ausgelöst.
- Die mobile Graphfläche und Toolbar wurden auf Touch-Bedienung angepasst.

## Projektstruktur

- Audits, Roadmap, Status und Release Notes liegen jetzt unter `docs/`.
- Die ZIP-Datei besitzt als obersten Ordner `Quantum Interactive Course/` und entspricht damit der lokalen Projektstruktur.
