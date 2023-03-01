class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    q = []
                    q.append((i,j))
                    temp = 0
                    for x,y in q:
                        if grid[x][y] == 1:
                            temp += 1
                            grid[x][y] = 0
                            for dx,dy in dirs:
                                if 0 <= x+dx < len(grid) and 0 <= y+dy < len(grid[0]) and grid[x+dx][y+dy] == 1:
                                    q.append((x+dx,y+dy))
                    maxArea = max(maxArea, temp)
        return maxArea