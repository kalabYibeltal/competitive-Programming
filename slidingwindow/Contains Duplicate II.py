class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    
# solution without sliding window
#         dictr = {}
#         for i in range(len(nums)):
#             if nums[i] in dictr:
#                 dictr[nums[i]].append(i)
#             else: dictr[nums[i]] = [i]
        
#         for i in dictr:
#             if dictr[i][0] != dictr[i][-1] and abs(dictr[i][0] - dictr[i][-1]) <= k: return True
            
        
        
        dictr = {}
 
        l = 0
        r = 0
        while r < len(nums):
            if r < k:
                if nums[r] in dictr and dictr[nums[r]] > 0: return True
                if nums[r] in dictr:
                    dictr[nums[r]] += 1
                else: dictr[nums[r]] = 1
                r += 1
            else:
                if nums[r] in dictr and dictr[nums[r]] > 0: return True
                if nums[r] in dictr:
                    dictr[nums[r]] += 1
                else: dictr[nums[r]] = 1
                dictr[nums[l]] -= 1
                l += 1
                r += 1
            
         
          
