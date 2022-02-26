class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        total=0
        i=0
        
        while i<len(grid):
            maxx=len(grid[0])-1
            minn=0
            while minn <= maxx:
                mid=(minn+maxx)//2
                # print(mid)
                if grid[i][mid]<0 and (mid==0 or (grid[i][mid-1])>=0):
                    # print(23456)
                    total = total + (len(grid[0])-mid)
                    # print(total)
                    break
                if grid[i][mid] >= 0:
                    minn=mid+1
                    # print(minn)
                elif grid[i][mid] < 0:
                    maxx=mid-1
                 
            i+=1
        return total
