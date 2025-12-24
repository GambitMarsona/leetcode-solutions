from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        nei = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for let in range(len(word)):
                pattern = word[:let] + "*" + word[let+1:]
                nei[pattern].append(word)

        q = deque([beginWord])
        visited = set([beginWord])
        res = 1 
        while q:
            for i in range(len(q)):    
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visited:
                            visited.add(neiWord) 
                            q.append(neiWord)
            res += 1
        return 0