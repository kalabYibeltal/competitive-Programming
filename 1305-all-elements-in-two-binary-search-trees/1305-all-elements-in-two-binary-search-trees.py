# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        arr = []
        def dfs(node):
            nonlocal arr
            if not node: return
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)
        
        dfs(root1)
        dfs(root2)
        
        arr.sort()
        return arr    
            