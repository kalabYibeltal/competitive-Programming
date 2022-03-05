# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        que=collections.deque([root])
        que2=collections.deque([0])
        ans=[root.val]
        count=[1]
       
        while que:
            current = que.popleft()
            level = que2.popleft()
            
            if len(ans)-1==level:
                ans[level]+=current.val
            else:
                ans.append(current.val)
            if len(count)-1==level:
                count[level]+=1
            else:
                count.append(1)
                
                
            if current.left:
                que.append(current.left)
                que2.append(level+1)
            if current.right:
                que.append(current.right)
                que2.append(level+1)
       
        
        i=0
        fans=[0]*len(ans)
        while i < len(ans):
            fans[i]=ans[i]/count[i]
            i+=1
        return fans
