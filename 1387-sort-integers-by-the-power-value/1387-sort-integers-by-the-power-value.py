class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        @lru_cache(None)
        def dp(n):
            if n == 1:
                return 0
            if n%2 == 0:
                return 1 + dp(n/2)
            return 1 + dp(3*n +1)
        
        arr = []
        for num in range(lo, hi + 1):
            arr.append([dp(num), num])
            print(dp(num))
        
        arr.sort()
        return arr[k-1][1]