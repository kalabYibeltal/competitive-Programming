class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l = -1 
        r =0
        ans = 1
        # if len(arr) : return len(arr)
        while r < len(arr) - 1:
            if r % 2 == 0:
                if arr[r] < arr[r+1]:
                    r += 1
                    # print(r)
                    ans = max(ans,r-l)
                else:
                    l = r 
                    r += 1
            else:
                if arr[r] > arr[r+1]:
                    r += 1
                    ans = max(ans,r-l)
                else:
                    l = r
                    r += 1
        
        l = -1
        r = 0
        while r < len(arr) - 1:
            if r % 2 == 0:
                if arr[r] > arr[r+1]:
                    r += 1
                    ans = max(ans,r-l)
                else:
                    l = r 
                    r += 1
            else:
                if arr[r] < arr[r+1]:
                    r += 1
                    ans = max(ans,r-l)
                else:
                    l = r
                    r += 1
        return ans
