# import osmnx as ox
# import os
# import streamlit as st
# from src.config import GRAPH_FILE_DRIVE, SPEED_CONFIG

# class MapLoader:
#     def load_graph(self):
#         filename = GRAPH_FILE_DRIVE
#         if not os.path.exists(filename):
#             st.error(f"Không tìm thấy file dữ liệu: {filename}")
#             st.warning("Vui lòng chạy file `python setup_data.py` để tải dữ liệu bản đồ 'drive' trước.")
#             st.stop()
            
#         G = ox.load_graphml(filename)
#         for u, v, k, data in G.edges(keys=True, data=True):
#             if 'weight' in data:
#                 try:
#                     data['weight'] = float(data['weight'])
#                 except (ValueError, TypeError):
#                     data['weight'] = 1.0
            
#             if 'length' in data:
#                 try:
#                     data['length'] = float(data['length'])
#                 except:
#                     data['length'] = 1.0


#         G = self._recalc_weight_for_motorbike(G)
             
#         return G

#     def _recalc_weight_for_motorbike(self, G):
#         bike_speed_kmh = SPEED_CONFIG.get("bike", 30) 
#         bike_speed_ms = bike_speed_kmh / 3.6  
        
#         for u, v, k, data in G.edges(keys=True, data=True):
#             length = data.get('length', 1.0)
#             data['weight'] = length / bike_speed_ms
            
#         return G

# def get_nearest_node(G, point):
#     return ox.distance.nearest_nodes(G, point[1], point[0])