from task1 import metro_graph


def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph.nodes()}
    distances[start] = 0
    visited = set()

    while visited != set(graph.nodes()):
        current_node = None
        min_distance = float('inf')
        for node in set(graph.nodes()) - visited:
            if distances[node] < min_distance:
                current_node = node
                min_distance = distances[node]

        visited.add(current_node)
        for neighbor, weight in graph[current_node].items():
            distance = distances[current_node] + weight['weight']
            if distance < distances[neighbor]:
                distances[neighbor] = distance

    path = [end]
    while end != start:
        for neighbor, weight in graph[end].items():
            if distances[end] - weight['weight'] == distances[neighbor]:
                path.append(neighbor)
                end = neighbor
                break

    return path[::-1]


dijkstra_path = dijkstra(metro_graph, "Борщагівка", "Мінська")
print("DIJKSTRA:\nшлях:", dijkstra_path)
