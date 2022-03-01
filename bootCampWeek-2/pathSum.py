# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def depthfinder(head:'node', target:int, summ):
    if head==None:
        return 0
    if head.left==None and head.right==None:
        return head.val
    summ= summ + head.val
    if head.left==None:
        y = depthfinder(head.right,target,summ)
        if (summ + y)==target:
            return head.val + y
    elif head.right==None:
        x = depthfinder(head.left,target, summ)
        if (summ + x)==target:
            return head.val + x
    else:
        x = depthfinder(head.left,target, summ)
        y = depthfinder(head.right,target,summ)
        if (summ + x)==target:
            return head.val + x
        elif (summ + y)==target:
            return head.val + y
    return -100000


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root==None:
            return 0
        if depthfinder(root,targetSum,0)==targetSum:
            return True
        return False
