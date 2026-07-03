from collections import deque, defaultdict

graph = defaultdict(list)

def add_edge(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)

add_edge(graph, "Sentinel", "CloudShield")
add_edge(graph, "Sentinel", "AutoPilot")
add_edge(graph, "Sentinel", "Guardian")
add_edge(graph, "CloudShield", "Responder")
add_edge(graph, "Guardian", "Responder")

def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

    return order

result = bfs(graph, "Sentinel")
print("BFS order from Sentinel:", result)

def bfs_distances(graph, start):
    visited = {start}
    distance = {start: 0}
    queue = deque([start])

    while queue:
        node = queue.popleft()
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                distance[neighbour] = distance[node] + 1
                queue.append(neighbour)

    return distance

distances = bfs_distances(graph, "Sentinel")
print("Distances from Sentinel:", distances)

def shortest_path(graph, start, end):
    visited = {start}
    parent = {start: None}
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node == end:
            break
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                parent[neighbour] = node
                queue.append(neighbour)

    path = []
    node = end
    while node is not None:
        path.append(node)
        node = parent[node]
    path.reverse()
    return path

path = shortest_path(graph, "Sentinel", "Responder")
print("Shortest path Sentinel -> Responder:", path)