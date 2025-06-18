class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = list(range(1,n+1,1))
        i = 0
        while len(queue) > 1:
            i = (i+k-1)%n
            queue.pop(i)
            n = len(queue)
        return queue[0]