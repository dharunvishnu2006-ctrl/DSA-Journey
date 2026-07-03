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

def dfs_iterative(graph, start):
    visited = {start}
    stack = [start]
    order = []

    while stack:
        node = stack.pop()
        order.append(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                stack.append(neighbour)

    return order

order_recursive = dfs_recursive(graph, "Sentinel")
print("DFS (recursive) order from Sentinel:", order_recursive)

order_iterative = dfs_iterative(graph, "Sentinel")
print("DFS (iterative) order from Sentinel:", order_iterative)

def has_cycle(graph, node, visited, parent):
    visited.add(node)
    for neighbour in graph[node]:
        if neighbour not in visited:
            if has_cycle(graph, neighbour, visited, node):
                return True
        elif neighbour != parent:  
            return True
    return False

visited = set()
cycle_found = has_cycle(graph, "Sentinel", visited, None)
print("Cycle detected:", cycle_found)

def count_components(graph, all_nodes):
    visited = set()
    components = 0

    for node in all_nodes:
        if node not in visited:
            components += 1
            dfs_recursive(graph, node, visited, [])   
    return components

graph["Isolated"]   
all_nodes = ["Sentinel", "CloudShield", "AutoPilot", "Guardian", "Responder", "Isolated"]
print("Connected components:", count_components(graph, all_nodes))