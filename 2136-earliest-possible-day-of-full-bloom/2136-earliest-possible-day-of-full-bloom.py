class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        A=[[i,j] for i ,j in zip(plantTime,growTime)]
        A=sorted(A,key=lambda x:x[1],reverse=True)
        
        ans=-1
        date=-1
        for i , j in A:
            date+=i
            ans=max(ans,date+j+1)
        return ans