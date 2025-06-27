class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # graph -> outgoing to nodes 
        n = len(graph)
        safe = {}
        # function checking whether i-th node is safe
        def dfs(i):
            if i in safe:
                return safe[i] # true of false
            # initialy safe[i] is set to false and later on it would be changed
            # if loop does not detect any cycle
            safe[i] = False
            # checking wheter neighbors will reach terminal node
            for nei in graph[i]:
                if dfs(nei) is False:
                    return safe[i]
            safe[i] = True
            return safe[i]

        res = []
        for i in range(n):
            if dfs(i):
                res.append(i)
        return res

