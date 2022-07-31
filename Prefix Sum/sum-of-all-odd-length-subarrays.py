class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        su = 0
        nums = arr
        for i, num in enumerate(nums):
            pre = num
            prev = num
            j = i
            while j < len(nums):
                if j + 2 < len(nums):
                    prev = prev + nums[j+1] + nums[j+2]
                    pre = pre + prev
                    # print(pre, prev)
                j += 2
            
            # print(pre)
            su += pre
        
        return su
