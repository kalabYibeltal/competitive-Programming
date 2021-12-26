class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        x=Counter(arr)
        ar=[]
        for c in x:
            ar.append([c,x[c]])
        q=sorted(ar,key=lambda e:-e[1])
        i=0
        y=0
        c=0
        while i<len(q):
            if y>=len(arr)/2:
                break
            else:
                y=y+q[i][1]
                c+=1
            i+=1
        return c
