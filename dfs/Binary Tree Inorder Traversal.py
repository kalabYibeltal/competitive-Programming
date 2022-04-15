# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        def trav(root):
            if not root:  return
            if root.left: trav(root.left)
            output.append(root.val)
            if root.right: trav(root.right)
            
            
        trav(root)
        return output
