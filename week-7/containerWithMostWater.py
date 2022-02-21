class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxh=0
        maxhn=0
        i=0
        j=len(height)-1
        while i< len(height):
            maxhn=min(height[i],height[j])*(j-i)
            if maxhn>=maxh:
                maxh=maxhn
            if height[i]>height[j]:
                print(i)
                j=j-1
            else:
                print(j)
                i=i+1
        return maxh
