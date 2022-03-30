# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
from collections import deque

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        def depthfinder(root):
            if not root:
                return 0
            return 1 + max(depthfinder(root.left),depthfinder(root.right))
        lev = depthfinder(root)

        arr=[root] 
        arr2=[]
        arr3=[]
        ans=[]
        i=0
        ans.append(root.val)
        while i < lev-1:
            j=0
            while j<len(arr):
                if arr[j].left:
                    arr2.append(arr[j].left)
                    arr3.append(arr[j].left.val)
                if arr[j].right:
                    arr2.append(arr[j].right)
                    arr3.append(arr[j].right.val)
                j+=1
            print(arr3)
            ans.append(max(arr3))
            arr3=[]
            arr=arr2
            arr2=[]
            i+=1
        return ans
        
