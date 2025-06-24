class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming = {i: 0 for i in range(1,n+1)}
        outgoing = {i: 0 for i in range(1,n+1)}
        for pair in trust:
            outgoing[pair[0]] = outgoing[pair[0]] + 1
            incoming[pair[1]] = incoming[pair[1]] + 1
        for i in range(1,n+1):
            if incoming[i] == n-1 and outgoing[i] == 0:
                return i
        return -1