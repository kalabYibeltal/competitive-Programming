class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for l in s:
            if l == "(":
                stack.append("(")
            else:
                ans = 0
                while stack[-1] != "(":
                    ans += stack.pop()
                stack.pop()
                if ans == 0:
                    stack.append(1)
                else:
                    stack.append(2*ans)
        
        return sum(stack)