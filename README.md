# 🚲 Wetter- & Ausleihverhalten-Analyse (Projektarbeit)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-orange?style=for-the-badge&logo=jupyter)
![License](https://img.shields.io/github/license/Bemnyyy/Projektarbeit?style=for-the-badge)

## 🎯 Projektübersicht

Dieses Repository enthält die vollständige Implementierung einer Projektarbeit, die sich der **datenanalytischen Untersuchung des Ausleihverhaltens von NextBike im Kontext verschiedener Wetterbedingungen** widmet.

Das Kernziel ist es, einen statistischen Zusammenhang zwischen gesammelten Wetterdaten (Temperatur, Niederschlag, etc.) und den NextBike-Nutzungsdaten herzustellen, um Muster und Rückschlüsse auf die Mobilitätsgewohnheiten der Nutzer zu ziehen.

---

### 🌟 Hauptfunktionen

* **API-Scraping:** Automatisierte Erfassung von Wetterdaten über externe APIs.
* **Datenverarbeitung:** Speicherung der gesammelten Daten in SQL-Datenbanken (`.db`-Dateien).
* **Datenanalyse:** Durchführung von Analysen, Korrelationen und Visualisierungen in interaktiven Jupyter Notebooks.
* **Wetterdaten:** Integration von Datenquellen wie OpenWeatherMap und Meteostat.

## 🛠️ Technologien & Stack

| Kategorie | Technologie | Beschreibung |
| :--- | :--- | :--- |
| **Sprache** | Python (3.x) | Die Basis für Datenverarbeitung und Skripte. |
| **Analyse** | Jupyter Notebook | Interaktive Umgebung für Analysen und Visualisierungen. |
| **Datenbank** | SQLite (implizit) | Speicherung der gesammelten Roh- und Prozessdaten. |
| **Bibliotheken** | `requirements.txt` | Alle notwendigen Python-Abhängigkeiten (z.B. Pandas, Matplotlib, Meteostat-Lib). |

## 🚀 Erste Schritte

Befolge diese Schritte, um das Projekt lokal einzurichten und auszuführen.

### 1. Repository klonen

Klone das Projekt auf deinen lokalen Rechner:

```bash
git clone [https://github.com/Bemnyyy/Projektarbeit.git](https://github.com/Bemnyyy/Projektarbeit.git)
cd Projektarbeit
```

### 2. Abhängigkeiten installieren

Alle benötigten Python-Bibliotheken sind in der `requirements.txt` aufgeführt

pip install -r requirements.txt

### 3. API-Konfiguration (Wichtig!)

Die Skripte zur Wetterdatenerfassung benötigen API-Schlüssel (Key).

# 1. Registrierung: Erstelle einen kostenlosen Account bei einem der folgenden Dienste:
- OpenWeatherMap: https://openweathermap.org/api
- Meteostat: https://dev.meteostat.net/api/

# 2. Konfigurationsdatei: Erstelle eine Konfigurationsdatei (z.B. config.py oder api_keys.py), welche deine generierten API-Schlüssel sicher enthält, damit die Python-Skripte (`Meteostat_Weather.py`, `Weather_API_scraping.py`) darauf zugreifen können.

!!! Hinweis: Der kostenlose Basis-Plan ist in der Regel ausreichend. Achte dennoch auf die maximal erlaubten Abfragen pro Tag/Monat. 

### 💻 Nutzung der Skripte & Analyse
Das Projekt ist in zwei Hauptphasen unterteilt: Datenakquise und Datenanalyse.

Phase 1: Datenakquise (Scraping)
Führe die Python-Scraping-Skripte aus, um die Wetterdaten zu sammeln. Diese Skripte erstellen die notwendigen SQL-Datenbanken (.db-Dateien) im Projektverzeichnis.

```bash
# Beispiel: Ausführen des Meteostat Scraping-Skripts
python Meteostat_Weather.py
```

Phase 2: Analyse mit Jupyter
Sobald die Datenbanken gefüllt sind, kannst du die Analysen in den Jupyter Notebooks durchführen:

1. Starte den Jupyter Notebook Server im Projektverzeichnis:

```bash
jupyter notebook
```

2. Öffne die relevanten Notebooks (z.B. Test_nextbike_notebook.ipynb oder Test_weather_notebook.ipynb).

3. Führe die Zellen nacheinander aus, um die Daten zu laden, zu verarbeiten und die Ergebnisse zu visualisieren.

### 📧 Kontakt & Support
Bei Fragen, Anregungen oder Problemen kannst du gerne ein Issue direkt in diesem GitHub-Repository erstellen.

### 📜 Lizenz
Dieses Projekt steht unter der MIT-Lizenz. Details dazu findest du in der Datei `LICENSE`.
