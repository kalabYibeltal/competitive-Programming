class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        pro = 1
        count = l =r = 0
        
        while r < len(nums) and l < len(nums):
            if pro * nums[r] >= k:
                pro = pro / nums[l]
                if pro < k:
                    n = r - l 
                    count += int(n * (n+1) /2)
                    n = r -l -1
                    a = int(n * (n+1) /2)
                    count -= a
                    print(a,r,l,count)
                    
                l += 1
            
            else:
                pro = pro * nums[r]
                r += 1
        
        # print(l,r)
        if pro < k:
            n = r - l 
            count += int(n * (n+1) /2)
            
            
        return count
            
