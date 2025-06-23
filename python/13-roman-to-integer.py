class Solution:
    def romanToInt(self, s: str) -> int:
        words = {
            "I" : 1,
            "V": 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        res = 0
        l = 0
        while l < len(s)-1: 
            if words[s[l]] < words[s[l+1]]:
                res = res + words[s[l+1]] - words[s[l]]
                l+=2
            else: 
                res += words[s[l]]
                l+=1
        if words[s[len(s)-1]] <= words[s[len(s)-2]]:
            res += words[s[len(s)-1]]
        return res
