class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        su = 0
        for i, num in enumerate(customers):
            if grumpy[i] == 0: su += num
        
        l = r = 0
        s = 0
        ans = 0
        while r < len(customers):
            if (r-l) >= minutes:
                if grumpy[l] == 1:
                    s -= customers[l]
                l += 1
            
            else: 
                if grumpy[r] == 1:
                    s += customers[r]
                    ans = max(ans,s)
                r += 1
        
        return ans + su
        
