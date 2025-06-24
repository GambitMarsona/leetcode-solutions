class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()
        nrow,ncol = len(image), len(image[0])
        org_color = image[sr][sc]
        def bfs(row,col):
            image[row][col] = color
            visited.add((row,col))
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            for dr,dc in directions:
                r,c = dr + row, dc + col
                if (r in range(nrow) and
                    c in range(ncol) and
                    image[r][c] == org_color and 
                    (r,c) not in visited):
                    bfs(r,c)
        bfs(sr,sc)
        return image