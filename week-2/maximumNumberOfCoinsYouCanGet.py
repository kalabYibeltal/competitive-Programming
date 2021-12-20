class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        x=len(piles)/3
        piles.sort()
        i=len(piles)-2
        count=0
        summ=0
        while count<x:
            summ=summ+piles[i]
            i=i-2
            count+=1
        return summ
