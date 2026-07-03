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
graph["Isolated"]   

def dfs_recursive(graph, node, visited=None, order=None):
    if visited is None:
        visited = set()
    if order is None:
        order = []
    visited.add(node)
    order.append(node)
    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs_recursive(graph, neighbour, visited, order)
    return order

def find_all_paths(graph, start, end, path=None):
    if path is None:
        path = []

    path = path + [start]

    if start == end:
        return [path]

    paths = []

    for neighbour in graph[start]:
        if neighbour not in path:
            new_paths = find_all_paths(graph, neighbour, end, path)
            paths.extend(new_paths)

    return paths

def count_components(graph, all_nodes):
    visited = set()
    components = 0
    for node in all_nodes:
        if node not in visited:
            components += 1
            dfs_recursive(graph, node, visited, [])
    return components

def is_graph_connected(graph, all_nodes):
    return count_components(graph, all_nodes) == 1

all_nodes = ["Sentinel", "CloudShield", "AutoPilot", "Guardian", "Responder", "Isolated"]

print("All paths Sentinel -> Responder:", find_all_paths(graph, "Sentinel", "Responder"))
print("Is graph fully connected?", is_graph_connected(graph, all_nodes))