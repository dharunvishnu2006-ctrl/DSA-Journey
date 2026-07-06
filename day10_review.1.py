def count_components(n, edges):
    parent = list(range(n))
    rank = [0] * n
    components = n  

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])  
        return parent[x]

    def union(x, y):
        nonlocal components
        rx, ry = find(x), find(y)

        if rx == ry:
            return False  
        if rank[rx] < rank[ry]:
            parent[rx] = ry
        elif rank[rx] > rank[ry]:
            parent[ry] = rx
        else:
            parent[ry] = rx
            rank[rx] += 1

        components -= 1  
        return True
    for u, v in edges:
        union(u, v)
    return components