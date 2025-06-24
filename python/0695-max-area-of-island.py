class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        visited = set()
        nrow, ncol = len(grid), len(grid[0])
        curr_max = 0
        def dfs(row,col):
            if (row not in range(nrow) or 
                   col not in range(ncol) or
                   (row,col) in visited or
                   grid[row][col] == 0):
                   return 0
            visited.add((row,col))
            area = 1
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            for rd, cd in directions:
                r,c = row + rd, col + cd
                area += dfs(r,c)
            return area

        for r in range(nrow):
            for c in range(ncol):
                if (r,c) not in visited:
                    curr_max = max(dfs(r,c),curr_max)
        return curr_max
