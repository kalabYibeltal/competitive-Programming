class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def times(t):
            summ = 0
            for i in time:
                if i > t: break
                summ += t//i
            return summ
        
        
        time.sort()
        left = 1
        right = time[0] * totalTrips
        while left <= right:
            mid = (left+right)//2
            x = times(mid)
            if x >= totalTrips:
                ans = mid
                right = mid - 1
            elif x < totalTrips: left = mid + 1
        return ans
            
            
            
            
