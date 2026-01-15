import heapq
import time
import networkx as nx

class DijkstraSolver:
    def __init__(self, graph):
        self.graph = graph

    def find_shortest_path(self, start_node, end_node):
        start_time = time.time()
        
        queue = [(0, start_node)]
        distances = {node: float('infinity') for node in self.graph.nodes}
        distances[start_node] = 0
        previous_nodes = {node: None for node in self.graph.nodes}
        visited = set()

        while queue:
            current_cost, current_node = heapq.heappop(queue)

            if current_node in visited:
                continue
            visited.add(current_node)

            if current_node == end_node:
                break

            for neighbor, edge_data in self.graph[current_node].items():
                
                all_weights = []
                for attr in edge_data.values():
                    w = attr.get('weight', 1)
                    try:
                        val = float(w) 
                    except (ValueError, TypeError):
                        val = 1.0 
                    all_weights.append(val)
                
                weight = min(all_weights) if all_weights else 1.0
                new_cost = current_cost + weight

                if new_cost < distances[neighbor]:
                    distances[neighbor] = new_cost
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(queue, (new_cost, neighbor))

        path = []
        current = end_node
        if previous_nodes[end_node] is not None or start_node == end_node:
            while current is not None:
                path.append(current)
                current = previous_nodes[current]
        path = path[::-1]

        execution_time = (time.time() - start_time) * 1000
        return path, distances[end_node], execution_time

    def compare_with_networkx(self, start_node, end_node):
        start_time = time.time()
        nx_path = nx.dijkstra_path(self.graph, start_node, end_node, weight='weight')
        nx_time = (time.time() - start_time) * 1000
        return nx_time