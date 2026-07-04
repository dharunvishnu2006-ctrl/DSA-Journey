def floyd_warshall(nodes, edges):
    dist = {u: {v: float('inf') for v in nodes} for u in nodes}
    for node in nodes:
        dist[node][node] = 0                  

    for u, v, weight in edges:
        dist[u][v] = weight                     
        dist[v][u] = weight                    
    for k in nodes:  
        for i in nodes:                 
            for j in nodes:              
                if dist[i][k] + dist[k][j] < dist[i][j]:  
                    dist[i][j] = dist[i][k] + dist[k][j] 

    return dist
nodes = ["Sentinel", "CloudShield", "AutoPilot", "Guardian", "Responder"]
edges = [
    ("Sentinel", "CloudShield", 4),
    ("Sentinel", "AutoPilot", 1),
    ("Sentinel", "Guardian", 7),
    ("CloudShield", "Responder", 2),
    ("Guardian", "Responder", 3),
]
result = floyd_warshall(nodes, edges)
print("Distance from CloudShield to Guardian:", result["CloudShield"]["Guardian"])