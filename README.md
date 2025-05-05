# HTML Rezept-Template & HTML zu PNG Konverter

Eine einfache HTML/CSS-Vorlage für Rezepte. Mit dem beiliegenden Python-Skript 'to_image.py' kann aus dem HTML-Dokument ein PNG-Bild erstellt werden..

## Funktionsweise

1. Du erstellst dein Rezept in einer HTML-Datei (z. B. `ananaskekse.html`).
2. Mit dem Python-Skript wird daraus ein Screenshot (`ananaskekse.png`) generiert.
3. So erhältst du ein optisch ansprechendes Bild deines Rezepts.

## 🛠️ Voraussetzungen

- Python 3

Folgendes muss danach noch installiert werden, um das Skript anwenden zu können:

```bash
pip install playwright
```

## Anwendung

Das erzeugt 'ananaskekse.png'.

```bash
python to_image.py ananaskekse.html
```

Die Breite kann man auch als Parameter angeben, standardmäßig ist diese auf 1052px (maximale Content-Breite auf Pr0gramm):

```bash
python to_image.py ananaskekse.html 1000
```
