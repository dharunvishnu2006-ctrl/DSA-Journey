import heapq
from collections import defaultdict

weighted_graph = defaultdict(list)

def add_weighted_edge(graph, u, v, w):
    graph[u].append((v, w))
    graph[v].append((u, w))

add_weighted_edge(weighted_graph, "Sentinel", "CloudShield", 4)
add_weighted_edge(weighted_graph, "Sentinel", "AutoPilot", 1)
add_weighted_edge(weighted_graph, "Sentinel", "Guardian", 7)
add_weighted_edge(weighted_graph, "CloudShield", "Responder", 2)
add_weighted_edge(weighted_graph, "Guardian", "Responder", 3)


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    heap = [(0, start)]

    while heap:
        current_dist, node = heapq.heappop(heap)
        if current_dist > distances[node]:
            continue
        for neighbour, weight in graph[node]:
            distance = current_dist + weight
            if distance < distances[neighbour]:
                distances[neighbour] = distance
                heapq.heappush(heap, (distance, neighbour))

    return distances

def shortest_distance_to(graph, start, target):
    distances = dijkstra(graph, start)
    return distances[target]

def has_path_under_cost(graph, start, target, max_cost):
    distance = shortest_distance_to(graph, start, target)
    return distance <= max_cost

print("Shortest distance Sentinel -> Responder:", shortest_distance_to(weighted_graph, "Sentinel", "Responder"))
print("Is Sentinel -> Guardian under cost 10?", has_path_under_cost(weighted_graph, "Sentinel", "Guardian", 10))
print("Is Sentinel -> Guardian under cost 5?", has_path_under_cost(weighted_graph, "Sentinel", "Guardian", 5))