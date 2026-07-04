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
def farthest_pair(nodes, edges):
    dist = floyd_warshall(nodes, edges)
    max_dist = -1
    best_pair = None

    for i in nodes:
        for j in nodes:
            if i != j and dist[i][j] != float('inf'):
                if dist[i][j] > max_dist:
                    max_dist = dist[i][j]
                    best_pair = (i, j)

    return best_pair, max_dist

def is_all_pairs_connected(nodes, edges):
    dist = floyd_warshall(nodes, edges)

    for i in nodes:
        for j in nodes:
            if dist[i][j] == float('inf'):
                return False
    return True

print("Farthest pair:", farthest_pair(nodes, edges))
print("Is fully connected?", is_all_pairs_connected(nodes, edges))