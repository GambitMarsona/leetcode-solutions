class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for index, word in enumerate(strs):
                if i >= len(word) or word[i] != strs[0][i]:
                    return res
                if index == len(strs) - 1:
                    res += strs[0][i]
        return res