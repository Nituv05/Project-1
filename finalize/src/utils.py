# src/utils.py
import osmnx as ox
import streamlit as st
import pandas as pd

# Code cũ 
def get_coordinates_from_name(place_name):
    """
    Chuyển đổi tên địa danh thành tọa độ (Lat, Long).
    Thêm hậu tố ', Hanoi' để tăng độ chính xác.
    """
    if not place_name:
        return None
    try:
        # Thêm context "Hanoi, Vietnam" để tránh tìm ra địa danh trùng tên ở nước khác
        query = f"{place_name}, Hanoi, Vietnam"
        # ox.geocode trả về (lat, lon)
        coords = ox.geocode(query)
        return coords
    except Exception as e:
    # Không tìm thấy địa điểm trên OSM
        return None


