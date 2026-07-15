from collections import deque
def shortest_path(self, start, target):
    visited = {start}
    queue = deque([(start, [start])])  

    while queue:
        node, path = queue.popleft()
        if node == target:
            return path
        for neighbour in self.graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour, path + [neighbour]))

    return None