class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tok in tokens:
            if tok not in ["+", "*", "/", "-"]:
                stack += [int(tok)]
            else:
                b = stack.pop()
                a = stack.pop()
                if tok == "+":
                    stack.append(a+b)
                elif tok == "-":
                    stack.append(a-b)
                elif tok == "*":
                    stack.append(a*b)
                else:
                    stack.append(int(a/b))
        return stack[0] 