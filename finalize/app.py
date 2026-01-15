import streamlit as st
import folium
from streamlit_folium import st_folium
import osmnx as ox
from src.map_loader import MapLoader, get_nearest_node
from src.utils import get_coordinates_from_name
from src.algorithms import DijkstraSolver
from src.config import COLORS
from src.nodeinfor import get_node_info

st.set_page_config(page_title="Hanoi Mini Map", layout="wide")

st.title("Hanoi Routing App")

with st.sidebar:
    st.header("Cấu hình lộ trình")
    st.info("Dữ liệu đang được tải")
    loader = MapLoader()
    mode = 'bike'
    G = loader.load_graph()
    st.success("Đã tải bản đồ thành công!")
    
   
    st.subheader("Chọn điểm ")
    start_input = st.text_input("Điểm đi ", value="Hồ Gươm")
    end_input = st.text_input("Điểm đến ", value="Đại học Quốc gia Hà Nội")
    
    run_btn = st.button("Tìm đường")

col1, col2 = st.columns([3, 1])
path_coords = []
stats = {}
default_start = (21.028511, 105.854167) 
default_end = (21.0368, 105.7824)
start_lat, start_lon = default_start
end_lat, end_lon = default_end
if run_btn:
    with st.spinner("Đang xử lý dữ liệu..."):
        start_coords = get_coordinates_from_name(start_input)
        end_coords = get_coordinates_from_name(end_input)
        if not start_coords or not end_coords:
            st.stop()
            
        error_msg = []
        if not start_coords:
            error_msg.append(f"Không tìm thấy địa điểm: **{start_input}**")
        if not end_coords:
            error_msg.append(f"Không tìm thấy địa điểm: **{end_input}**")
            
        if error_msg:
            for err in error_msg:
                st.error(err)
                st.info("Gợi ý: Hãy thử nhập tên cụ thể hơn.")
        else:
            start_node, dist_start = ox.distance.nearest_nodes(G, start_coords[1], start_coords[0], return_dist=True)
            end_node, dist_end = ox.distance.nearest_nodes(G, end_coords[1], end_coords[0], return_dist=True)
            
            THRESHOLD_METER = 2000 
            valid_locations = True
            
            if dist_start > THRESHOLD_METER:
                st.error(f"Địa điểm **{start_input}** nằm quá xa bản đồ hỗ trợ.")
                valid_locations = False
            if dist_end > THRESHOLD_METER:
                st.error(f"Địa điểm **{end_input}** nằm quá xa bản đồ hỗ trợ.")
                valid_locations = False
            
            if valid_locations:
                solver = DijkstraSolver(G)
                path, cost, exec_time = solver.find_shortest_path(start_node, end_node)
                nx_time = solver.compare_with_networkx(start_node, end_node)
                path_coords = [] 
                total_meters = 0
                
                for u, v in zip(path[:-1], path[1:]):
                    edge_data = G.get_edge_data(u, v)[0]
                    total_meters += float(edge_data.get('length', 0))
                    if 'geometry' in edge_data:
                        xs, ys = edge_data['geometry'].xy
                        path_coords.extend(list(zip(ys, xs)))
                    else:
                        point_u = (G.nodes[u]['y'], G.nodes[u]['x'])
                        point_v = (G.nodes[v]['y'], G.nodes[v]['x'])
                        path_coords.extend([point_u, point_v])
                readable_path = []
                for node_id in path:
                    info = get_node_info(G, node_id)
                    readable_path.append(info)
                stats = {
                    "num_nodes": len(path),
                    "cost": cost, 
                    "dist_km": total_meters / 1000, 
                    "path_list": readable_path,              
                    "my_algo_time": exec_time,
                    "nx_algo_time": nx_time
                }
                
                start_lat, start_lon = start_coords
                end_lat, end_lon = end_coords

with col1:
    center_lat = (start_lat + end_lat) / 2
    center_lon = (start_lon + end_lon) / 2
    m = folium.Map(location=[center_lat, center_lon], zoom_start=14)
    folium.Marker([start_lat, start_lon], popup="Start", icon=folium.Icon(color="green")).add_to(m)
    folium.Marker([end_lat, end_lon], popup="End", icon=folium.Icon(color="red")).add_to(m)
    
    if path_coords:
        folium.PolyLine(
            path_coords, 
            color=COLORS.get(mode, "blue"), 
            weight=5, 
            opacity=0.8,
            tooltip=f"Lộ trình {mode}"
        ).add_to(m)

    st_folium(m, width="100%", height=600, returned_objects=[])

with col2:
    st.subheader("Kết quả")
    if stats:
        st.metric("Quãng đường", f"{stats['dist_km']:.2f} km")
        st.metric("Số node đi qua", stats['num_nodes'])
        
        with st.expander("Chi tiết lộ trình"):
            steps = stats['path_list']
            compact_steps = []
            if steps:
                compact_steps.append(steps[0])
                for i in range(1, len(steps)):
                    if steps[i] != steps[i-1]:
                        compact_steps.append(steps[i])
            
            for idx, step in enumerate(compact_steps):
                st.text(f"{idx + 1}. {step}")
            
    else:
        st.info("Nhập địa điểm bên trái và nhấn **Tìm đường** để xem kết quả.")