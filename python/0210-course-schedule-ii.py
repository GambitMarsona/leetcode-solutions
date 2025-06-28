class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        numprereq = [0] * numCourses
        
        for a,b in prerequisites:
            graph[b].append(a)
            numprereq[a] += 1
        
        q = collections.deque([i for i in range(numCourses) if numprereq[i] == 0])
        order = []

        while q:
            course = q.popleft()
            order.append(course)
            for neighbor in graph[course].copy():
                graph[course].remove(neighbor)
                numprereq[neighbor] -= 1
                if numprereq[neighbor] == 0:
                    q.append(neighbor)
        
        return order if len(order) == numCourses else []


        
        
        