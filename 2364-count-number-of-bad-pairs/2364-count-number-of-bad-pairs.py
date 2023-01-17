class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        for i in range(len(nums)):
            freq[nums[i]-i] += 1
        count = 0
        # print(freq)
        for diff in freq:
            # print(diff)
            count += freq[diff] * (len(nums) - freq[diff])
        
        return count//2