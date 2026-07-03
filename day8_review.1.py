from collections import defaultdict
graph = defaultdict(list)

def add_edge(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)

add_edge(graph, "Sentinel", "CloudShield")
add_edge(graph, "Sentinel", "AutoPilot")
add_edge(graph, "Sentinel", "Guardian")
add_edge(graph, "CloudShield", "Responder")
add_edge(graph, "Guardian", "Responder")

def is_connected(graph, u, v):
    return v in graph[u]

def count_edges(graph):
    total = 0
    for neighbors in graph.values():
        total += len(neighbors)
    return total // 2

print("Sentinel-CloudShield connected?", is_connected(graph, "Sentinel", "CloudShield"))
print("Sentinel-Responder connected?", is_connected(graph,"Sentinel","Responder"))
print("Total edges:", count_edges(graph))