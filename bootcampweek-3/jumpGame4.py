import collections
from collections import deque


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        # que  = collections.deque([[0,0]])
        que = collections.deque([0])
        level = collections.deque([0])
       
        visited=set()
        visited.add(0)
        dictr={}
        i=len(arr)-1
        print(len(arr))
        while i >=0:
            if arr[i] in dictr:
                dictr[arr[i]].append(i)
            else:
                dictr[arr[i]]=[i]
            i-=1
    
                        
                
                
        while que:
            cur=que.popleft()
            lev=level.popleft()
            # print(cur[0])                     
            
                                  
            if(cur==len(arr)-1):
                return lev
            if cur-1 >=0 and cur-1 not in visited:
                
                que.append(cur-1)
                level.append(lev+1)
                visited.add(cur-1)
                
                
            if cur+1 < len(arr) and cur+1 not in visited:
                que.append(cur+1)
                level.append(lev+1)
                visited.add(cur+1)
            if arr[cur] in dictr:
                x=dictr[arr[cur]]
                for m in x:
                    if m not in visited:
                        que.append(m)
                        level.append(lev+1)
                        visited.add(m)
                del(dictr[arr[cur]])       
                    
                    
                    
                    
                
