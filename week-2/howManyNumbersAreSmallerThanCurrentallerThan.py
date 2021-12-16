class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n=len(nums)
        i=0
        
        arr=[0]*n
        while(i<n):
            j=0
            count=0
            while(j<n):
                if(nums[i]>nums[j]):
                    count+=1
                j+=1
            arr[i]=count
            i+=1
        return arr
