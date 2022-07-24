class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 1: return nums[0] == target
        
        def helper(nums,target,start,end):
            mid = (start+end)//2
            if start >= end: return False
            if nums[start] == target or nums[mid] == target or nums[end] == target: return True
            if start == mid: return False
            elif nums[start] < nums[mid]:
                if nums[start] < target < nums[mid]:
                    return helper(nums,target,start,mid)
                else:
                    return helper(nums,target,mid,end)
            elif nums[mid] < nums[end]:
                if nums[mid] < target < nums[end]:
                    return helper(nums,target,mid,end)
                else:
                    return helper(nums,target,start,mid)
            else:
                return helper(nums,target,start,mid) or helper(nums,target,mid,end)
        
        return helper(nums,target,0,len(nums)-1)
