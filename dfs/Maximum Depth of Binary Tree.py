# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depth(total):
            if total == None: return 0
            elif total.left==None and total.right==None: return 1
            elif not total.left and total.right:
                t = depth(total.right)
            elif total.left and not total.right:
                t = depth(total.left)
            else:
                t = max(depth(total.left),depth(total.right))
            return t + 1
        
        return depth(root)
