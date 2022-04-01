class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        ans = -1
        while left <= right:
            mid = (left+right)//2
            if (mid+1 < len(nums) and nums[mid] > nums[mid+1]):
                ans = mid + 1
                break
            if nums[left] > nums[mid]:
                if (mid-1 > -1 and nums[mid - 1] > nums[mid]):
                    ans = mid - 1
                    break
                right =  mid-1
            else:
                if mid + 1 < len(nums) and nums[mid+1] < nums[mid]:
                    ans =  mid + 1
                    break
                left = mid + 1
        print (ans)
        if not( 0 < ans < len(nums)): left = 0
        else: left = ans
        right = len(nums) - 1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target: return mid
            if target > nums[mid]: left = mid + 1
            else: right = mid - 1
        left = 0
        right = ans
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target: return mid
            if target > nums[mid]: left = mid + 1
            else: right = mid - 1
        return -1
        
