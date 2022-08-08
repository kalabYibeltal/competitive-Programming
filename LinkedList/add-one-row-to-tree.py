# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def tr(node,h):
            if not node: return 
            if h == depth - 1:
                # if node.left: 
                l = node.left
                temp = TreeNode(val)
                node.left = temp
                temp.left = l
                # else:
                #     temp = TreeNode(val)
                #     node.left = temp
                # if node.right: 
                r = node.right
                temp = TreeNode(val)
                node.right = temp
                temp.right = r
#                 else:
#                     temp = TreeNode(val)
#                     node.right = temp
                
                return 
            else:
                tr(node.left,h+1)
                tr(node.right,h+1)
        
        if depth == 1:
            temp = TreeNode(val)
            temp.left = root
            return temp
        tr(root,1)
        return root
        
                                            
