class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        j=0
        arr = []
        while(j<len(nums)):
            if(nums[j]==target):
                arr.append(j)
            j+=1
        return arr
