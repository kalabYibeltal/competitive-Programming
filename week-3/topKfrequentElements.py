class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x=Counter(nums)
        print(x)
        #dictr=defaultdict(int)
        arr=[]
        i=0
        for c in x:
            arr.append([c,x[c]])
        q=sorted(arr,key=lambda e:e[1])
        print(q)
        i=len(q)-1
        arrt=[]
        while k>0:
            arrt.append(q[i][0])
            i=i-1
            k=k-1
        return arrt
