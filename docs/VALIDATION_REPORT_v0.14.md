# Validierungsbericht v0.14

## Geprüfte Punkte

- lokale Links, Anker, Quellpfade und eingebettete Dateien;
- JavaScript-Syntax der geänderten Navigations- und Mathematikmodule;
- vollständige Entfernung aktiver MathJax-2-Referenzen;
- Vorhandensein des eigenständigen lokalen MathJax-3-SVG-Bundles;
- direkte dynamische Formeldarstellung über `tex2svgPromise()`;
- Off-Canvas-Verhalten der mobilen Etappenleiste;
- volle Inhaltsbreite bei geschlossener mobiler Navigation;
- bestehende numerische Modelltests und Runtime-Smoke-Tests.

## Einschränkung

Eine pixelbasierte Chromium-Prüfung war in der Build-Umgebung weiterhin nicht reproduzierbar ausführbar: der bereitgestellte Chromium-Prozess beendet lokale Seitenaufrufe nicht zuverlässig. Deshalb wurden DOM-Struktur, JavaScript, Dateiverweise, Renderer-Konfiguration und mathematische TeX-Konvertierung unabhängig geprüft.

## Ergebnisse

- 0 fehlerhafte lokale Links, Anker oder Quellenpfade;
- 40/40 numerische Modellprüfungen bestanden;
- 4/4 Runtime-Smoke-Tests bestanden;
- 251/251 verifizierte Kursformeln mit derselben MathJax-3-TeX-Engine erfolgreich in SVG konvertiert;
- keine aktive Referenz auf `MathJax.Hub` oder das entfernte MathJax-2-Verzeichnis;
- v0.12-, v0.13- und v0.14-Regressionsprüfungen bestanden.
