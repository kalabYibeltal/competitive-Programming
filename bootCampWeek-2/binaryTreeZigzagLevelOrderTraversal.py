# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []
        que=collections.deque([root])
        que2=collections.deque([0])
        ans=[]
       
        while que:
            current = que.popleft()
            level = que2.popleft()
            
            if len(ans)-1==level:
                ans[-1].append(current.val)
            else:
                ans.append([])
                ans[-1].append(current.val)
         
                
            if current.left:
                que.append(current.left)
                que2.append(level+1)
            if current.right:
                que.append(current.right)
                que2.append(level+1)
       
       
        i=0
        while i < len(ans):
            if i%2!=0:
                print(1)
                ans[i].reverse()
            i+=1
        return ans
