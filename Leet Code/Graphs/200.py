#Number of Islands
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0,-1),(1,0),(0,1),(-1,0)]
        island = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    q = deque()
                    q.append((i,j))
                    while q:
                        x,y = q.popleft()
                        if grid[x][y] == "1":
                            grid[x][y] = "0"
                            for dx,dy in directions:
                                if 0 <= x+dx < len(grid) and 0 <= y+dy < len(grid[0]) and grid[x+dx][y+dy] == "1":
                                    q.append((x+dx,y+dy))
                    island = island + 1
        return island
                
                        