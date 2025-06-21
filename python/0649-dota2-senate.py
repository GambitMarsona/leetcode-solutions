from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        self.r = deque()
        self.d = deque()
        n = len(senate)
        for i in range(len(senate)):
            if senate[i] == "R":
                self.r.append(int(i))
            else:
                self.d.append(int(i))
        while self.r and self.d:
            if self.r[0] < self.d[0]:
                self.d.popleft()
                self.r.append(n)
                n += 1
                self.r.popleft()
            else:
                self.r.popleft()
                self.d.append(n)
                n += 1
                self.d.popleft()
        if self.d:
            return "Dire"
        else:
            return "Radiant"
