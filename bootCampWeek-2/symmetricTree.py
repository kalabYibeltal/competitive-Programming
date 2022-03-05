# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


import collections
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        visited=[]
       # print(root.left.val)
        if (root.left==None and root.right==None):
            return True
        if (root.left and root.right==None) or (root.right and root.left==None):
            return False
        que = collections.deque([root.left])
        que2 = collections.deque([root.right])
      
        bool=True
   
    
        while que:
            
            current = que.popleft()
            
            current2 = que2.popleft()
            
            if (current2==None) and que2:
                # print(current2.val)
                current2 = que2.popleft()  
            if (current==None) and que:
                current = que.popleft() 
            # print(current.val)
            # print(current2.val)
            
            if current.val != current2.val:
                return False
            if current.left:
                que.append(current.left)
            
            if current.right:
                que.append(current.right)   
            
            if current2.right:
                que2.append(current2.right)
                
            if current2.left:
                que2.append(current2.left)
                # print(que2)
            
                
            if (current.left and current2.right==None) or (current2.right and current.left==None):
                return False
            if (current2.left and current.right==None) or (current.right and current2.left==None):
                return False
            # print(que2)
        return True  
                
        
        
        
        
        
        
