class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        minn=0
        maxx=len(nums)-1
        arr=[]
        while minn<=maxx:
            mid=(minn+maxx)//2
            if nums[mid]==target and (mid==0 or nums[mid-1]!=target):
                arr.append(mid)
                break
            elif nums[mid]>=target:
                maxx=mid
            if minn==mid:
                minn+=1
            elif nums[mid] < target:
                minn=mid
            
        minn=0
        maxx=len(nums)-1
        
        while minn<=maxx:
            mid=(minn+maxx)//2
            if nums[mid]==target and (mid+1==len(nums) or nums[mid+1]!=target):
                arr.append(mid)
                break
            elif nums[mid]>target:
                maxx=mid
            if minn==mid:
                minn+=1
            elif nums[mid] <= target:
                minn=mid
                
                
        if len(arr)!=2:
            return [-1,-1]
        else:
            return arr
