class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 1, len(arr) - 2
        
        while l <= r:
            mid = (l+r)// 2
            
            if arr[mid-1] < arr[mid] > arr[mid+1]:
                return mid
            
            if arr[mid-1] < arr[mid] < arr[mid+1]:
                l = mid + 1
            
            else:
                r = mid - 1
                