class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dictr={}
        i=0
        while i<len(s):
            if s[i] in dictr:
                dictr[s[i]].append(i)
            else:
                dictr[s[i]]=[i]
            i+=1
        print(dictr)
        arr=[]
        x=0
        c=0
        for i in dictr:
            if dictr[i][0]<=x<dictr[i][-1]:
                x=dictr[i][-1]
                c=c+len(dictr[i])
                # print(i,x,'a')
            elif dictr[i][0]>x:
        
                arr.append(c)
                
                c=len(dictr[i])
                x=dictr[i][-1]
               
            else: 
                # print(i,x,'c')
                c=c+len(dictr[i])
        # arr.pop(0)
        if sum(arr)<len(s):
            arr.append(c)
        return arr
        
