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


agents = ["Sentinel", "CloudShield", "AutoPilot", "Guardian", "Responder"]
index = {agent: i for i, agent in enumerate(agents)}
matrix = [[0 for _ in range(len(agents))] for _ in range(len(agents))]

def add_edge_matrix(matrix, u, v):
    i = index[u]
    j = index[v]
    matrix[i][j] = 1
    matrix[j][i] = 1

add_edge_matrix(matrix, "Sentinel", "CloudShield")
add_edge_matrix(matrix, "Sentinel", "AutoPilot")
add_edge_matrix(matrix, "Sentinel", "Guardian")
add_edge_matrix(matrix, "CloudShield", "Responder")
add_edge_matrix(matrix, "Guardian", "Responder")

def remove_edge(graph, u, v):
    if v in graph[u]:
        graph[u].remove(v)
    if u in graph[v]:
        graph[v].remove(u)

def print_neighbours(graph, node):
    if node in graph:
        print(f"Neighbours of {node}: {graph[node]}")
    else:
        print("Node not found")

print("Adjacency List:")
for node in graph:
    print(node, "->", graph[node])

print()

print_neighbours(graph, "Sentinel")

print("\nRemoving edge: Guardian <-> Responder")
remove_edge(graph, "Guardian", "Responder")

print("\nUpdated Adjacency List:")
for node in graph:
    print(node, "->", graph[node])

print("\nAdjacency Matrix:")
print("              ", "  ".join(agents))
for i, row in enumerate(matrix):
    print(f"{agents[i]:12}", row)