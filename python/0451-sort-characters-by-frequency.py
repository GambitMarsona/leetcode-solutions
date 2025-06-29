import collections
class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        bucket = defaultdict(list)

        for char, cnt in counter.items():
            bucket[cnt].append(char)
        res = []
        for i in range(len(s),0,-1):
            for elem in bucket[i]:
                res.append(elem*i)
        return "".join(res)
            