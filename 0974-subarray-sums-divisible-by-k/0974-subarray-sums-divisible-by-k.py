class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
      
        reminder = defaultdict(int)
        reminder[0] = 1
        running_sum = 0
        total = 0
        
        for num in nums:
            running_sum += num
            if num < 0:
                running_sum += k
            total += reminder[running_sum % k]
            reminder[running_sum % k] += 1
        
        return total
            