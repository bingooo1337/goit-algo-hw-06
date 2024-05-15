from task1 import metro_graph


def dfs_iterative(graph, start, end):
    visited = set()
    stack = [(start, [start])]
    iterations = 0

    while stack:
        iterations += 1
        (vertex, path) = stack.pop()
        if vertex not in visited:
            if vertex == end:
                return path, iterations
            visited.add(vertex)
            for neighbor in graph.neighbors(vertex):
                stack.append((neighbor, path + [neighbor]))

    return None, iterations


def bfs_iterative(graph, start, end):
    visited = set()
    queue = [(start, [start])]
    iterations = 0

    while queue:
        iterations += 1
        (vertex, path) = queue.pop(0)
        if vertex not in visited:
            if vertex == end:
                return path, iterations
            visited.add(vertex)
            for neighbor in graph.neighbors(vertex):
                queue.append((neighbor, path + [neighbor]))

    return None, iterations


dfs_path = dfs_iterative(metro_graph, "Борщагівка", "Мінська")
print("DFS:\nкількість ітерацій:", dfs_path[1], "\nдовжина:", len(
    dfs_path[0]), "\nшлях:", dfs_path[0], "\n")

bfs_path = bfs_iterative(metro_graph, "Борщагівка", "Мінська")
print("BFS:\nкількість ітерацій:", bfs_path[1], "\nдовжина:", len(
    bfs_path[0]), "\nшлях:", bfs_path[0])
