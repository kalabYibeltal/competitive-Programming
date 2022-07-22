# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None: return 0
        que = collections.deque([[root,1]])
        h = 0
        while que:
            root, val = que.popleft()
            if not root.left and not root.right: return val
            if root.left: que.append([root.left,val+1])
            if root.right: que.append([root.right,val+1])
         
                
