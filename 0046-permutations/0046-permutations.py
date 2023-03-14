class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        res = [-11] * len(nums)
      

        def fn(index):
            if index == len(nums):
                ans.append(res[:])
                return 
            for c in range(len(nums)):
                if res[c] == -11:   
                    res[c] = nums[index]
                    fn(index + 1)
                    res[c] = -11

        fn(0)
        return ans
        