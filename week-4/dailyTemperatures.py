class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        i=0
        ar=[0]*len(temperatures)
        stack=[]
        stack2=[]
        while i<len(temperatures):
            if len(stack)==0:
                stack.append(temperatures[i])
                stack2.append(i)
            else:
                while len(stack)>0:
                    if temperatures[i]>stack[-1]:
                        ar[stack2[-1]]=i-stack2[-1]
                        stack2.pop()
                        stack.pop()
                    else:
                        break
                stack.append(temperatures[i])
                stack2.append(i)
            i+=1
        return ar
