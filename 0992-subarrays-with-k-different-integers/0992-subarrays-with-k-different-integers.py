class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostK(nums, k):
            n = len(nums)
            left, right = 0, 0

            res = 0

            from collections import Counter
            counter = Counter()

            while right < n:
                counter[nums[right]] += 1

                while len(counter) > k:
                    counter[nums[left]] -= 1
                    if counter[nums[left]] == 0:
                        del counter[nums[left]]

                    left += 1

                res += right - left + 1
                right += 1

            return res
        
        return atMostK(nums, k) - atMostK(nums, k-1)