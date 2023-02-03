class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = path.split('/')
        answer = deque()
        counter = 0
        
        for i in range(len(stack)-1,-1,-1):
            if stack[i]:
                if stack[i] == '..':
                    counter += 1
                elif stack[i] != '.' and stack[i] != '..':
                    if counter > 0:
                        counter -= 1
                    else:
                        answer.appendleft('/'+stack[i])
        
        if len(answer) > 0:
            return ''.join(answer) 
        else:
            return '/'