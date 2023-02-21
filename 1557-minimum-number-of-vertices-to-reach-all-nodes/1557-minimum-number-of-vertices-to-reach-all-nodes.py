class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        ans = set(i for i in range(n))
        for i,j in edges:
            if j in ans: ans.remove(j)
        return ans