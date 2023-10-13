# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        
        def dfs(pre, post):
            
            if not pre:
                return None
            
            node = TreeNode(pre[0])
            if len(pre) == 1:
                return node
            
            for i in range(1,len(pre)):
                if pre[i] == post[-2]:
                    node.left = dfs(pre[1:i], post[:i-1])
                    node.right = dfs(pre[i:], post[i-1: len(post) - 1] )
                    return node
        return dfs(preorder, postorder)
            
            
            
            
            
            
            
            