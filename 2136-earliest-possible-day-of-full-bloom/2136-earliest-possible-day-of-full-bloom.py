class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        newArray = []
        for i in range(len(plantTime)):
            newArray.append([plantTime[i],growTime[i]])
        newArray=sorted(newArray,key=lambda x:x[1],reverse=True)
        ans=-1
        day=-1
        for p , q in newArray:
            day+=p
            ans=max(ans,day+q+1)
        return ans