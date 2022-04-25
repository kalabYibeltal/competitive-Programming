class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumhash = {}
        for n in range(0,len(nums)):
            if target - nums[n] in sumhash:
                return [n,sumhash[target - nums[n]]]
            sumhash[nums[n]] = n
        print(sumhash)
