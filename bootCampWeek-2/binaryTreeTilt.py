# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def summ(head):
    if head==None:
        return 0
    if head.left==None and head.right==None:
        return head.val
    if head.left==None:
        return head.val + summ(head.right)
    elif head.right==None:
        return head.val + summ(head.left)
    return head.val + summ(head.right) + summ(head.left)
    
def tilt(head):
    if head==None:
        return 0
    head.val=abs(summ(head.right) - summ(head.left))
    tilt(head.left)
    tilt(head.right)
    
    
    
    
    
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        tilt(root)
        return summ(root)
