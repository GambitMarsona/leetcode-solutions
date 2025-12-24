class Solution:
    def isPalindrome(self, x: int) -> bool: 
        if x < 0:
            return False
        if x <= 9:
             return True
        x = str(x)
        l = 0
        r = len(x)-1
        while x[l] == x[r] and l < r:
            l += 1 
            r -= 1
            if l == r or l == r+1:
                return True
        return False