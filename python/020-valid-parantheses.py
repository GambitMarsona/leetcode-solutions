class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis = {
            "{": "}",
            "(": ")",
            "[": "]"
                }
          
        stack = []
        i = 0 
        balanced = True
        while i < len(s) and balanced:
            if s[i] in parenthesis:
                stack += [s[i]]
            else: 
                if stack and s[i] ==  parenthesis[stack[-1]]:
                    stack.pop()
                else:
                    balanced = False
            i += 1 
        
        if balanced and len(stack) == 0:
            return balanced
        else:
            return False
                
                
                