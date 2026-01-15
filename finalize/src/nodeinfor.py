def get_node_info(G, node_id):
    node_data = G.nodes[node_id]
    lat = node_data['y']
    lon = node_data['x']
    street_names = set()
    
    try:
        for neighbor in G.neighbors(node_id):
            edge_data = G.get_edge_data(node_id, neighbor)
            for key, data in edge_data.items():
                name = data.get('name')
                if name:
                    if isinstance(name, list):
                        for n in name: street_names.add(n)
                    else:
                        street_names.add(name)
    except:
        pass 

    if street_names:
        location_str = ", ".join(list(street_names)[:2]) 
        return f"{location_str}"
    else:
        return f"Toạ độ ({lat:.4f}, {lon:.4f})"