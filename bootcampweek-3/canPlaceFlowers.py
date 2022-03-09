class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i=1
        if len(flowerbed)==1 and n==1 and flowerbed[0]==0:
            return True
        if flowerbed[0]==0 and len(flowerbed)>1 and flowerbed[1]==0:
            flowerbed[0]=1
            n=n-1
        while i<len(flowerbed)-1:
            if flowerbed[i-1]==0 and flowerbed[i+1]==0 and flowerbed[i]==0:
                flowerbed[i]=1
                n=n-1
            i+=1
        if len(flowerbed)>1 and flowerbed[-2]==0 and flowerbed[-1]==0:
            n=n-1
        if n<=0:return True
