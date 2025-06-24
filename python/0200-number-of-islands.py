class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        nrow, ncol = len(grid), len(grid[0])
        islands = 0
        def bfs(row,col):
            q = collections.deque()
            q.append((row,col))
            visited.add((row,col))
            while q:
                row,col = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in directions:
                    r,c = row + dr, col + dc
                    if (r in range(nrow) and
                        c in range(ncol) and
                        (r,c) not in visited and
                        grid[r][c] == "1"):
                        visited.add((r,c))
                        q.append((r,c))

        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c] == "1" and (r,c) not in visited:
                    islands += 1
                    bfs(r,c)
        return islands