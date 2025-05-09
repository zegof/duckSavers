# DuckScreenSaver 
## Deutsch (english below)

Ein kleiner, animierter Bildschirmschoner mit Enten, entwickelt mit PyQt5. Die Enten bewegen sich zufällig über den Bildschirm und prallen an den Bildschirmrändern ab. Perfekt für einen Hauch Chaos auf dem Desktop!

### Features

- 10 animierte Enten, die sich frei bewegen
- Transparenter Hintergrund
- Als `.exe` kompiliert und in `.scr` umbenannt – funktioniert als Windows-Bildschirmschoner
- Einfach anpassbar: Ersetze duck.png im selben Verzeichnis durch ein beliebiges Bild

### Verwendung

1. Lade eine der .scr-Dateien herunter:
   - [bouncyDuck.scr](bouncyDuck.scr)
   - [duckFly.scr](duckFly.scr)
2. Lege die Datei `duck.png` in denselben Ordner oder verwende ein eigenes Bild mit dem Namen `duck.png`.
   - [duck.png](duck.png)
3. Rechtsklick auf die `.scr` Datei und wähle **Installieren**.
4. Windows öffnet den Dialog für die Bildschirmschoner-Einstellungen.
5. Wähle "bouncyDuck" oder "duckFly" aus der Liste.

**Hinweis:** Antivirenprogramme könnten `.scr`-Dateien strenger prüfen – die Datei ist jedoch sicher und enthält keine Schadsoftware.

### Quellcode ausführen

Wenn du den Code selbst ausführen oder ändern willst:

#### Voraussetzungen

- Python 3.x
- PyQt5

Installation der Abhängigkeiten:

```bash
pip install PyQt5
```

Start des Programms:

```bash
python duck_screensaver.py
```

### Lizenz

Dieses Projekt steht unter der MIT License. Siehe die [LICENSE](LICENSE) Datei für Details.

---

# DuckScreenSaver
## English

A lightweight animated screensaver featuring cute ducks moving across your screen. Built with Python and PyQt5, and compiled into a `.scr` file for easy installation on Windows.

### Features

- 10 animated ducks moving randomly across the screen
- Transparent fullscreen display
- Runs as a standard `.scr` file on Windows
- Customizable: Replace `duck.png` in the same folder with your own image

### How to Use

1. Download one of the `.scr` files:
    - [bouncyDuck.scr](bouncyDuck.scr)
    - [duckFly.scr](duckFly.scr)
2. Place `duck.png` in the same directory, or use your own image named `duck.png`.
    - [duck.png](duck.png)
3. Right-click the `.scr` file and select **Install**.
4. Windows will open the Screen Saver Settings dialog.
5. Choose “bouncyDuck” or “duckFly” from the dropdown and apply.

**Note:** Some antivirus software may flag `.scr` files. This file is safe and does not contain malware.

### Running from Source

If you want to modify or run the code yourself:

#### Requirements

- Python 3.x
- PyQt5

Install dependencies:

```bash
pip install PyQt5
```

Run the script:

```bash
python bouncyDuck.py
```

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.