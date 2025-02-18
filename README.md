# Einladungsgenerator

Dieses Python-Skript liest eine Liste von Gästen aus einer Datei (`gaeste.txt`) und erstellt für jeden Gast eine individuelle Einladung als Textdatei.

## Funktionsweise

1. Das Skript öffnet die Datei `gaeste.txt` und liest Zeile für Zeile die Namen der Gäste aus.
2. Für jeden Namen wird eine personalisierte Einladung erstellt.
3. Die Einladung wird in einer eigenen Datei im Ordner `einladungen/` gespeichert.
4. Zusätzlich wird die Einladung im Terminal ausgegeben.

## Voraussetzungen

- Python 3.x
- Die Datei `gaeste.txt` muss im gleichen Verzeichnis wie das Skript vorhanden sein.
- Ein Ordner namens `einladungen` muss existieren, oder kann vorher manuell erstellt werden.

## Beispiel `gaeste.txt`

```
Anna
Ben
Clara
```

## Beispiel einer generierten Einladung (`einladungen/Anna.txt`)

```
Hallo Anna,

Ich möchte Dich gerne zu meinem Geburtstag einladen.

Viele Grüße

Marcus
```

## Nutzung

1. Stelle sicher, dass `gaeste.txt` die Namen der Gäste enthält.
2. Führe das Skript aus:
   ```sh
   python einladung.py
   ```
3. Die Einladungen werden im Ordner `einladungen/` als `.txt`-Dateien gespeichert.


