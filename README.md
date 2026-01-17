# 🚲 Wetter- & Ausleihverhalten-Analyse (Projektarbeit)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-orange?style=for-the-badge&logo=jupyter)
![License](https://img.shields.io/github/license/Bemnyyy/Projektarbeit?style=for-the-badge)

## 🎯 Projektübersicht

Dieses Repository enthält die Implementierung einer Projektarbeit, die das **Ausleihverhalten von NextBike im Kontext verschiedener Wetterbedingungen** datenanalytisch untersucht.  
Ziel ist es, statistische Zusammenhänge zwischen Wetterdaten (z.B. Temperatur, Niederschlag) und NextBike-Nutzungsdaten herzustellen, um Muster und Rückschlüsse auf die Mobilitätsgewohnheiten der Nutzer zu ermöglichen.

Die Projektarbeit richtet sich an den Hochschulkontext (Lehrveranstaltungen zu Digitalisierung, Mobilität und Datenanalyse) und soll eine reproduzierbare, nachvollziehbare Auswertung bereitstellen.

---

## 🌟 Hauptfunktionen

- **API-Scraping:** Automatisierte Erfassung von Wetterdaten über externe APIs (z.B. OpenWeatherMap, Meteostat).
- **Datenhaltung:** Speicherung der gesammelten Roh- und Prozessdaten in SQLite-Datenbanken (`.db`-Dateien).
- **Datenanalyse:** Durchführung von Analysen, Korrelationen und Visualisierungen in interaktiven Jupyter Notebooks.
- **Mobilitätsdaten:** Nutzung von NextBike-Ausleihdaten als Grundlage für die Betrachtung des Leihverhaltens.

---

## 🛠️ Technologien & Stack

| Kategorie    | Technologie     | Beschreibung |
| :----------- | :-------------- | :----------- |
| **Sprache**  | Python (3.x)    | Basis für Skripte, Datenverarbeitung und Analysen. |
| **Analyse**  | Jupyter Notebook| Interaktive Umgebung für explorative Datenanalyse und Visualisierung. |
| **Datenbank**| SQLite          | Lokale Speicherung der Wetter- und Ausleihdaten in `.db`-Dateien. |
| **Bibliotheken** | `requirements.txt` | Enthält alle Python-Abhängigkeiten (z.B. Pandas, Matplotlib, Meteostat). |

---

## 🚀 Erste Schritte

### 1. Repository klonen

```bash
git clone https://github.com/Bemnyyy/Projektarbeit.git
cd Projektarbeit
