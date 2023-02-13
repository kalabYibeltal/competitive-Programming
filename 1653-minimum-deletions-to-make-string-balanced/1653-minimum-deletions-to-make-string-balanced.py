class Solution:
    def minimumDeletions(self, s: str) -> int:
        stack = []
        count = 0
        
        for c in s:
            
            if not stack:
                stack.append(c)
                
            elif c == 'a' and stack[-1] == 'b':
                count += 1
                stack.pop()
            
            else:
                stack.append(c)
            
        return count