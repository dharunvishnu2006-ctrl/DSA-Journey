def numIslands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
            return                  
        grid[r][c] = '0'             
        dfs(r + 1, c)              
        dfs(r - 1, c)              
        dfs(r, c + 1)              
        dfs(r, c - 1)             

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1          
                dfs(r, c)             
    return count

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(numIslands(grid))

class GraphNode:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node):
    if not node:
        return None
    visited = {}                       

    def dfs(original):
        if original in visited:
            return visited[original]     

        clone = GraphNode(original.val)
        visited[original] = clone         

        for neighbor in original.neighbors:
            clone.neighbors.append(dfs(neighbor))
        return clone

    return dfs(node)
n1 = GraphNode(1)
n2 = GraphNode(2)
n3 = GraphNode(3)
n4 = GraphNode(4)

n1.neighbors = [n2, n4]
n2.neighbors = [n1, n3]
n3.neighbors = [n2, n4]
n4.neighbors = [n1, n3]

cloned = cloneGraph(n1)
print(cloned.val, [n.val for n in cloned.neighbors])

def pacificAtlantic(heights):
    if not heights:
        return []

    rows, cols = len(heights), len(heights[0])
    pacific = set()
    atlantic = set()

    def dfs(r, c, visited, prev_height):
        if (r < 0 or r >= rows or c < 0 or c >= cols or
            (r, c) in visited or heights[r][c] < prev_height):
            return                     
        visited.add((r, c))
        dfs(r + 1, c, visited, heights[r][c])
        dfs(r - 1, c, visited, heights[r][c])
        dfs(r, c + 1, visited, heights[r][c])
        dfs(r, c - 1, visited, heights[r][c])

    for c in range(cols):
        dfs(0, c, pacific, heights[0][c])           
        dfs(rows - 1, c, atlantic, heights[rows - 1][c]) 

    for r in range(rows):
        dfs(r, 0, pacific, heights[r][0])           
        dfs(r, cols - 1, atlantic, heights[r][cols - 1])  
    return [list(cell) for cell in pacific & atlantic]   
heights = [
  [1,2,2,3,5],
  [3,2,3,4,4],
  [2,4,5,3,1],
  [6,7,1,4,5],
  [5,1,1,2,4]
]
print(pacificAtlantic(heights))

from collections import deque

def orangesRotting(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh_count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c, 0))    
            elif grid[r][c] == 1:
                fresh_count += 1
    minutes_passed = 0
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while queue:
        r, c, minute = queue.popleft()
        minutes_passed = max(minutes_passed, minute)

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2                   
                fresh_count -= 1
                queue.append((nr, nc, minute + 1))
    return minutes_passed if fresh_count == 0 else -1

grid = [
  [2,1,1],
  [1,1,0],
  [0,1,1]
]
print(orangesRotting(grid))