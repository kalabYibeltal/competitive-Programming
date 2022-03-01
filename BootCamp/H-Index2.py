class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h=0
        n=len(citations)
        # i=0
        # while i<len(citations):
        #     if citations[i]>=n-i:
        #         h=n-i
        #         break
        #     i+=1
        # return h
#         the above code also works
       
        minn=0
        maxx=n-1

        if citations[-1]==0:
            return 0
        if len(citations)==1:
            return 1
        while minn < maxx:
            mid=(minn+maxx)//2
            if citations[mid]>=n-mid:
                maxx=mid
            else:
                minn=mid+1
                mid=(minn+maxx)//2 
        return n-mid
