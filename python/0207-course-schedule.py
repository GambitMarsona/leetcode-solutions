from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # implementation of Khan's algorithm
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        count = 0

        while q:
            node = q.popleft()
            count += 1
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        return count == numCourses





