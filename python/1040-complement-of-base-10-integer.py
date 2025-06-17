class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1      
        
        stack = []
        while n > 0:
            rest = n % 2
            stack.append(rest)
            n = n // 2
        reverse_stack = []
        while stack:
            reverse_stack.append(stack.pop())

        num = {
            1 : 0,
            0 : 1
            }
        i = 0
        while reverse_stack and i < len(reverse_stack):
            reverse_stack[i] = num[reverse_stack[i]]
            i += 1 

        res = 0 
        i = 0
        while reverse_stack:
            res += reverse_stack.pop() * (2 ** i)
            i += 1

        return res