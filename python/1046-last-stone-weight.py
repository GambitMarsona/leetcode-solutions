import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            larger = heapq.heappop(stones)
            smaller = heapq.heappop(stones)
            if larger - smaller != 0:
                heapq.heappush(stones, larger-smaller)
        return abs(stones[0]) if stones else 0
