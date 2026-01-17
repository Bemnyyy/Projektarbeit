Die bestehende README ist bereits klar strukturiert und gut verständlich; sinnvoll wäre vor allem eine stärkere Trennung zwischen „Projekt (wissenschaftliche Arbeit)“ und „Code-Repository“, etwas mehr Kontext zu Datenquellen sowie ein kurzer Hinweis zu Limitierungen und Reproduzierbarkeit. [mobidata-bw](https://mobidata-bw.de/dataset/?res_format=GeoJSON&tags=Bike-Sharing)

## Überarbeiteter README-Entwurf

```markdown
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
```

### 2. Virtuelle Umgebung (empfohlen)

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# oder
.\.venv\Scripts\activate    # Windows

pip install --upgrade pip
```

### 3. Abhängigkeiten installieren

```bash
pip install -r requirements.txt
```

---

## 🔑 API-Konfiguration (Wichtig)

Für die Wetterdatenerfassung werden API-Schlüssel benötigt.

1. **Registrierung bei Wetterdiensten**
   - OpenWeatherMap: https://openweathermap.org/api  
   - Meteostat: https://dev.meteostat.net/api/

2. **Konfigurationsdatei anlegen**

Erstelle z.B. eine Datei `api_keys.py` im Projektverzeichnis, die deine Schlüssel enthält (wird **nicht** versioniert):

```python
# api_keys.py (Beispiel)
OPENWEATHER_API_KEY = "DEIN_OPENWEATHER_KEY"
METEOSTAT_API_KEY = "DEIN_METEOSTAT_KEY"
```

Die Skripte (`Meteostat_Weather.py`, `Weather_API_scraping.py` o.ä.) greifen auf diese Variablen zu.

> Hinweis: Kostenlose Pläne sind in der Regel ausreichend, beachte aber die Limits für API-Aufrufe.

---

## 🚴 NextBike-Daten bereitstellen

Die verwendeten NextBike-Daten müssen lokal heruntergeladen und im Projektordner abgelegt werden.

- NextBike-Daten (Download-Link, wie in der Projektbeschreibung verwendet):  
  https://bwsyncandshare.kit.edu/s/ReyJrRRzaFYMXtf?openfile=true

Speichere die Dateien im gleichen Ordner wie die Skripte, die diese Daten einlesen (z.B. Analyse-Notebooks oder Import-Skripte).

---

## 💻 Nutzung der Skripte & Analyse

Das Projekt ist in zwei Hauptphasen gegliedert: **Datenakquise** und **Datenanalyse**.

### Phase 1: Datenakquise (Scraping)

Führe die Python-Skripte zur Wetterdatenerfassung aus, um die Datenbanken zu befüllen:

```bash
# Beispiel: Meteostat-Scraping
python Meteostat_Weather.py

# Beispiel: OpenWeather-Scraping
python Weather_API_scraping.py
```

Die Skripte erzeugen bzw. aktualisieren entsprechende SQLite-Datenbanken (`.db`) im Projektverzeichnis.

### Phase 2: Analyse mit Jupyter

1. Jupyter im Projektordner starten:

```bash
jupyter notebook
```

2. Relevante Notebooks öffnen, z.B.:
   - `Test_nextbike_notebook.ipynb`
   - `Test_weather_notebook.ipynb`

3. Zellen nacheinander ausführen, um:
   - Daten aus den `.db`-Dateien zu laden
   - Daten zu bereinigen und zu aggregieren
   - Korrelationen und Visualisierungen zu erzeugen

---

## 📊 Reproduzierbarkeit & Hinweise

- Die Ergebnisse hängen von:
  - dem verwendeten Zeitraum der NextBike-Daten,
  - der Verfügbarkeit/Historie der Wetterdaten der APIs
  ab. Bei Änderungen der Datenbasis können sich Kennzahlen und Grafiken leicht unterscheiden.
- API-Schlüssel, lokal erzeugte Datenbanken und Rohdatendateien werden aus Datenschutz- und Lizenzgründen nicht eingecheckt.

---

## 📧 Kontakt

Bei Fragen, Anregungen oder Problemen kann ein Issue in diesem Repository erstellt werden.  
Alternative Kontaktwege können bei Bedarf in der Projektarbeit selbst angegeben werden.

---

## 📜 Lizenz

Dieses Projekt steht unter der **MIT-Lizenz**.  
Details sind der Datei `LICENSE` zu entnehmen.
```

Wenn du magst, kann der Text noch stärker auf „Karlsruhe / KVV.nextbike“ oder deinen konkreten Untersuchungszeitraum zugeschnitten werden (z.B. eigener Abschnitt „Untersuchungsgebiet & Zeitraum“).
