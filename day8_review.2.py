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

def is_reachable(graph, start, end):
    distances = bfs_distances(graph, start)
    return end in distances
def nodes_within_k_hops(graph, start, k):
    distances = bfs_distances(graph, start)
    return [node for node, dist in distances.items() if dist <= k]

print("Sentinel reach Responder?", is_reachable(graph, "Sentinel", "Responder"))
print("Sentinel reach Isolated?", is_reachable(graph, "Sentinel", "Isolated"))  
print("Nodes within 1 hop of Sentinel:", nodes_within_k_hops(graph, "Sentinel", 1))