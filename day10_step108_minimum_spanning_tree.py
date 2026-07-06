class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))   

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False  
        self.parent[root_x] = root_y
        return True

def kruskal_mst(n, edges):
    edges.sort()                     
    uf = UnionFind(n)               
    mst_cost = 0
    mst_edges = []

    for weight, u, v in edges:
        if uf.union(u, v):           
            mst_cost += weight
            mst_edges.append((u, v, weight))

    return mst_cost, mst_edges    