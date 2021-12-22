class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        print(changed)
        arr=[]
        n=len(changed)
        if n%2!=0:
            return arr
        i=0
        p=Counter(changed) 
        while i<n:
            if changed[i]==0 and p[changed[i]]>0:
                arr.append(changed[i]) 
                x=changed[i]
                p[2*x]=p[2*x]-2
                if p[2*x]<0:
                    return []
            elif p[changed[i]]>0:
                arr.append(changed[i])
                x=changed[i]
                p[2*x]=p[2*x]-1
                p[x]=p[x]-1
                if p[2*x]<0:
                    return []
            i=i+1
        return arr
