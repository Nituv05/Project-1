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
