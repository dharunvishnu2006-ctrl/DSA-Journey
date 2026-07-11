from collections import deque, defaultdict

def topological_sort(num_nodes, edges):
    graph = defaultdict(list)
    in_degree = [0] * num_nodes
    
    for u, v in edges:        
        graph[u].append(v)
        in_degree[v] += 1
    
    queue = deque([node for node in range(num_nodes) if in_degree[node] == 0])
    result = []   
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    if len(result) != num_nodes:      
        return []                   
    return result
edges = [(0, 1), (2, 3)]
print(topological_sort(4, edges))

def topological_sort_dfs(num_nodes, edges):
    graph = defaultdict(list)
    for u, v in edges:                 
        graph[u].append(v)
    
    visited = [False] * num_nodes
    result = []
    
    def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
        result.append(node)                
    for node in range(num_nodes):
        if not visited[node]:
            dfs(node)
    
    result.reverse()               
    return result
edges = [(0, 1), (2, 3)]
print(topological_sort_dfs(4, edges))

def has_cycle(num_nodes, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
    
    visited = [False] * num_nodes
    rec_stack = [False] * num_nodes
    
    def dfs(node):
        visited[node] = True
        rec_stack[node] = True
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor):
                    return True
            elif rec_stack[neighbor]:   
                return True
        
        rec_stack[node] = False            
        return False
    
    for node in range(num_nodes):
        if not visited[node]:
            if dfs(node):
                return True   
    return False

edges_with_cycle = [(0,1), (1,2), (2,0)]
print(has_cycle(3, edges_with_cycle))   
edges_no_cycle = [(0,1), (1,2)]
print(has_cycle(3, edges_no_cycle)) 

def can_finish(num_courses, prerequisites):
    edges = [(b, a) for a, b in prerequisites]
    return not has_cycle(num_courses, edges)
print(can_finish(2, [[1, 0]]))         
print(can_finish(2, [[1, 0], [0, 1]]))      