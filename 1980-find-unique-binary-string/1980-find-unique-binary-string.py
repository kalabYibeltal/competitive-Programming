class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        num = set([int(x,2) for x in nums])
        for i in range(pow(2, len(nums[0])) ):
            if i not in num:
                return '0'*(len(nums[0]) - len(bin(i)[2:]) )   + bin(i)[2:]
