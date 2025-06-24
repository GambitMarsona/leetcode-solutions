class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        graph = collections.defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        seen = set()
        seen.add(source)
        def dfs(node):
            if node == destination:
                return True
            for conn_node in graph[node]:
                if conn_node not in seen:
                    seen.add(conn_node)
                    if dfs(conn_node):
                        return True
            return False
        return dfs(source)
