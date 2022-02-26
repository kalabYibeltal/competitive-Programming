# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    return version

class Solution:
    def firstBadVersion(self, n: int) -> int:
        minn=1
        maxx=n
        
        a=False
        while True:
            mid= (minn+maxx)//2
            print(isBadVersion(0))
            x=isBadVersion(mid)
            if x==True and isBadVersion(mid-1)==False:
                return mid
            elif x==False and isBadVersion(mid+1)==True:
                return mid+1
            else:
                if x==True:
                    maxx=mid
                else:
                    minn=mid
            
            
            
            
        
