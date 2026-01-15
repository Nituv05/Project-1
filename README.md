# Hanoi Routing App 

A pathfinding application for Hanoi, Vietnam, built with Python (Streamlit) and real-world OpenStreetMap data.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)

## Features

* **Optimal Routing:** Implements **Dijkstra's Algorithm** to find the shortest path between any two locations in Hanoi.
* **Real-world Data:** Uses `OSMnx` to fetch actual road networks, including street types and speed limits.
* **Interactive Map:** Visualizes the route, start/end points using `Folium`.
* **Detailed Analytics:** Provides path distance (km), number of nodes, and street names.
* **Performance Comparison:** Compares custom Dijkstra implementation against NetworkX's built-in algorithm.

## Project Structure

```text
Project-1/
├── finalize/
│   ├── app.py              # Main application entry point
│   ├── requirements.txt    # Python dependencies
│   ├── data/               # Stores .graphml map data (Generated locally)
│   └── src/                # Source code
│       ├── algorithms.py   # Dijkstra algorithm implementation
│       ├── map_loader.py   # Data loading and processing
│       ├── config.py       # Configuration settings
│       ├── utils.py 
|       └── nodeinfor.py
└── README.md               # Project documentation

## Installation & Setup

### 1. Clone this project

```bash
git clone [https://github.com/Nituv05/Project-1.git](https://github.com/Nituv05/Project-1.git)
cd Project-1

### 2. Install dependencies
``` bash
pip install -r finalize/requirements.txt

### 3. Data Setup 
The map data file for Hanoi (`hanoi_drive.graphml`) is approximately **160MB**, so it is **not included** in this GitHub repository. You must generate it locally before running the app.

The application is configured to automatically download the data if it is missing.

1.  Ensure you have an internet connection.
2.  Run the app (see step 4). The first launch will take **3-5 minutes** to download and process the map data from OpenStreetMap.
3.  Once finished, the data will be saved in `finalize/data/` for faster future loading.

### 4. Run the Application
Run the following command in your terminal:

```bash
streamlit run finalize/app.py
