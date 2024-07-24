# Image Overlay with Frame

Dieses Python-Skript fügt ein Overlay-Bild in ein Basisbild ein und platziert es im oberen rechten Eck mit einem roten Rahmen. Das resultierende Bild hat die Dimensionen des Basisbilds, und das Overlay-Bild nimmt etwa 40% der Breite des Basisbilds ein.

## Voraussetzungen

- Python 3.x
- Pillow-Bibliothek

Sie können Pillow mit dem folgenden Befehl installieren:

```sh
pip install pillow
```

## Verwendung

Führen Sie das Skript über die Kommandozeile mit den Pfaden zu den Basis-, Overlay- und Ausgabebildern als Argumente aus:

```sh
python add_image_in_frame.py path/to/base_image.jpg path/to/overlay_image.jpg path/to/output_image.jpg
```

### Beispiel

Angenommen, Sie haben ein Basisbild `base_image.jpg` und ein Overlay-Bild `overlay_image.jpg`. Sie möchten das resultierende Bild als `output_image.jpg` speichern. Verwenden Sie den folgenden Befehl:

```sh
python add_image_in_frame.py base_image.jpg overlay_image.jpg output_image.jpg
```

## Beschreibung des Programms

1. **Bilder laden**: Das Programm öffnet die Basis- und Overlay-Bilder.
2. **Größe des Overlay-Bilds anpassen**: Das Overlay-Bild wird auf 40% der Breite des Basisbilds verkleinert, wobei das Seitenverhältnis beibehalten wird.
3. **Rahmen hinzufügen**: Ein roter Rahmen wird um das Overlay-Bild hinzugefügt.
4. **Position berechnen**: Die Position für das Overlay-Bild wird so berechnet, dass es im oberen rechten Eck des Basisbilds platziert wird.
5. **Bilder kombinieren**: Das Overlay-Bild wird an der berechneten Position in das Basisbild eingefügt.
6. **Ergebnis speichern**: Das kombinierte Bild wird gespeichert.

## Autoren

- Marvin Seith

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert - siehe die [LICENSE](LICENSE) Datei für Details.