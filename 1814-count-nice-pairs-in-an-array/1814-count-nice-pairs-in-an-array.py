class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        count = 0
        for n in nums:
            diff = n - int(str(n)[::-1])
            count += dic[diff]
            dic[diff] += 1
            # print(diff)
            # print(dic[diff])
        
        return (count) % 1000000007