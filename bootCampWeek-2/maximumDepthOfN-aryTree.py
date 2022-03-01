"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
def depthfinder(head:'node'):
    maxx=0
    if len(head.children)==0:
        return 1
    for i in head.children:
        x=depthfinder(i)
        if x > maxx:
            maxx=x
    return 1 + maxx
    
    
    
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root==None:
            return 0
        return depthfinder(root)
