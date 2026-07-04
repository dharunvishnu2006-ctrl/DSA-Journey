def bellman_ford(edges, nodes, start):
    distances = {node: float('inf') for node in nodes}   
    distances[start] = 0                                  

    for i in range(len(nodes) - 1):       
        for u, v, weight in edges:        
            if distances[u] != float('inf') and distances[u] + weight < distances[v]: 
                distances[v] = distances[u] + weight    

    for u, v, weight in edges:
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            print("Negative cycle detected!")
            return None

    return distances
nodes = ["Sentinel", "CloudShield", "AutoPilot", "Guardian", "Responder"]
edges = [
    ("Sentinel", "CloudShield", 4),
    ("Sentinel", "AutoPilot", 1),
    ("Sentinel", "Guardian", 7),
    ("CloudShield", "Responder", 2),
    ("Guardian", "Responder", -5),   
]

result = bellman_ford(edges, nodes, "Sentinel")
print("Shortest distances from Sentinel:", result)