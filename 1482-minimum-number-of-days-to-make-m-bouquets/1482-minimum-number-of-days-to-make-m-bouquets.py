class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay): return -1
        
        def check(num):
            mc = 0
            kc = 0
            for val in bloomDay:
                if val > num:
                    kc = 0
                else:
                    kc += 1
                
                if kc == k:
                    mc += 1
                    kc = 0
             
            if mc >= m: return True
            return False
        
        sb = sorted(bloomDay)
        left , right = 0,  len(bloomDay) - 1
        
        while left < right:
            mid = (left + right)//2
            ans = check(sb[mid])
            if ans:
                right = mid
            else:
                left = mid + 1
        
        return sb[right]
        
        
        
        
        
        