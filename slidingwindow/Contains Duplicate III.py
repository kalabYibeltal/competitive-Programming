from sortedcontainers import SortedList
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
#         l = r = 0
#         for i in range(len(nums)):
#             for j in range(k):
#                 if i + j == len(nums): break
#                 if abs(nums[i] - nums[i+j]) <= t: return True
                
#         return False
        arr = SortedList()
        for i, num in enumerate(nums):
            if i > k:
                arr.remove(nums[i-k-1])
            
            pos1 =  bisect_left(arr,num-t)
            pos2 = bisect_right(arr,num+t)
            
            if pos1 != pos2:
                return True
            
            arr.add(num)
        
        return False
