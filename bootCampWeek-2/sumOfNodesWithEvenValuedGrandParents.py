# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def sum(node):
    summ=0
    if node.left and node.left.left:
        summ+=node.left.left.val
    if node.left and node.left.right:
        summ+=node.left.right.val
    if node.right and node.right.left:
        summ+=node.right.left.val
    if node.right and node.right.right:
        summ+=node.right.right.val
    return summ
def summer(node):
    if node==None:
        return 0
    else:
        if node.val%2==0:
            return sum(node) + summer(node.right) + summer(node.left)
        else:
            return summer(node.right) + summer(node.left)
        
        
#     if node.left==None and node.right==None:
#         if node.val%2==0:
#             return sum(node)
#     elif node.left==None:
#         if node.val%2==0:
#             return sum(node) + summer(node.right)
#         else:
#             summer(node.right)
#     elif node.right==None:
#         if node.val%2==0:
#             return sum(node) + summer(node.left)
#         else:
#             summer(node.right)
    
# if node.left:
#         summer(node.left)
        
        
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        return summer(root)
