# Projektarbeit

Dieses Repository enthält eine Projektarbeit, die hauptsächlich in Python und Jupyter Notebooks umgesetzt wurde. Der Fokus liegt auf datenanalytischer Verarbeitung und Programmierung mit Python. Hierbei sollen Wetterdaten gesammelt werden und im Anschluss mit Next-Bike Daten verglichen werden um auf das Ausleihverhalten zurückschließen zu können.

## Projektbeschreibung

Das Projekt umfasst Analysen, Visualisierungen und Programmieraufgaben, die in Jupyter Notebooks dokumentiert sind und API-Scraping Codes in Python. Es werden verschiedene Methoden der Datenverarbeitung und -auswertung angewandt.

## Technologien

- Jupyter Notebook
- Python
- Weitere Abhängigkeiten sind in den Notebooks und in der requirements.txt dokumentiert.

## API Scraping Hinweise

Für die Verwendung der API-Scraping-Skripte in diesem Projekt ist es notwendig, eigenständig einen Account bei OpenWeatherMap oder Meteostat zu erstellen. Dort muss ein API-Key generiert werden, der für die Abfrage der Wetterdaten erforderlich ist.

OpenWeatherMap: https://openweathermap.org/api

Meteostat/Rapid: https://dev.meteostat.net/api/

Der Basic / Kostenlose Plan reicht bei beiden aus, beachte dennoch die maximalen Abfragen!

Anschließend ist eine Konfigurationsdatei zu erstellen, die diese API-Keys enthält, damit die Scraping-Skripte darauf zugreifen können.

## Installation

1. Repository klonen:
git clone https://github.com/Bemnyyy/Projektarbeit.git

2. Jupyter Notebook installieren (falls noch nicht geschehen).

3. Abhängigkeiten installieren (siehe requierements.txt).

4. API Keys anlegen und Konfiguration erstellen (siehe oben).

## Nutzung

- Starte die .py Programme nachdem alle Abhängigkeiten installiert wurden und die Konfigurationsdatei angelegt wurden.

- Im Anschluss an werden SQL-Dateien erstellt welche in weiteren Schritten über die Notebooks dargestellt werden können.

- Starte Jupyter Notebook im Projektverzeichnis:
jupyter notebook

- Öffne die einzelnen Notebooks und führe die Zellen aus.

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Details findest du in der LICENSE-Datei.

## Kontakt

Bei Fragen und Anregungen bitte ein Issue im Repository öffnen.

---