class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        n=len(nums)
        i=0
        arr=[0]*n
        while(i<n):
            arr[i]=int(nums[i])
            i+=1
        arr.sort()
        return str(arr[-k])
