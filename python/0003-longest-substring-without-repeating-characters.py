class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        maximum = 0
        r = 0
        for l in range(len(s)):
            while r < len(s) and s[r] not in chars:
                chars.add(s[r])
                maximum = max(maximum, len(chars))
                r+=1
            if r < len(s) and s[r] in chars:
                chars.discard(s[l])
        return maximum