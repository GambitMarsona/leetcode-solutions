class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        odd = [0] * n

        def bfs(i):
            if odd[i]:
                return True
            odd[i] = -1
            q = collections.deque([i])
            while q:
                i = q.popleft()    
                for nei in graph[i]:
                    if odd[i] == odd[nei]:
                        return False
                    elif not odd[nei]:
                        q.append(nei)
                        odd[nei] = -1 * odd[i]

        # defining main loop
        for i in range(n):
            if bfs(i) is False:
                return False
        return True
        