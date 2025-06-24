class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        edges = collections.defaultdict(list)
        visited = set()
        n = len(isConnected)
        provinces = 0
        def dfs(start):
            visited.add(start)
            for end in range(n):
                if end not in visited and isConnected[start][end]:
                    dfs(end)  

        for start in range(n):
            if start not in visited:
                provinces += 1
                dfs(start)
        return provinces