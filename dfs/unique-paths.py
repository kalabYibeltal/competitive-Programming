class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dictr = {}
        def find(row,col):
            if row == m -1 and col == n - 1: return 1
            if (row,col) in dictr: return dictr[(row,col)]
            val = 0
            if row + 1 < m: val += find(row +1, col)
            if col + 1 < n: val += find(row, col + 1)
        
            dictr[(row,col)] = val
            return val
        
        return find(0, 0 )
