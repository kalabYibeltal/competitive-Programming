# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        arr = [[] for i in range(1000)]
        def dfs(node,lev,row):
            if not node: return 
            arr[lev+500].append([row,node.val])
            dfs(node.left,lev-1,row+1)
            dfs(node.right,lev+1,row+1)
        
        dfs(root,0,0)
        ans = []
        for i in arr:
            if i != []:
                i.sort()
                al = []
                for row,val in i:
                    al.append(val)
                ans.append(al)
        
        
        return ans
            
            