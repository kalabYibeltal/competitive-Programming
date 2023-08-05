class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        nums = [[sum([int(x) for x in str(num)]),num] for num in nums]
        nums.sort()
        
        answer = -1
        for i in range(len(nums) - 1):
            if nums[i][0] == nums[i+1][0]:
                answer = max(answer, nums[i][1] + nums[i+1][1])
                
        return answer
