class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # print(triangle[1][1])
        dictr = {}
        def total(i,j):
            if i == len(triangle): return 0
            if (i,j) in dictr: return dictr[(i,j)]
            ans =min(total(i+1,j),total(i+1,j+1)) + triangle[i][j]
            dictr[(i,j)]= ans
            return ans
        return total(0,0)
