class Solution:
    def sortSentence(self, s: str) -> str:
        
        arr=s.split()
        arr2=s.split()
        arr3=s.split()
        n=len(arr)
        
        i=1
        z=""
        while(i<n+1):
            x=arr3[i-1]
            j=0
            y=""
            while(j<(len(x)-1)):
                y=y+x[j]
                j+=1
            arr2[(int(arr[i-1][-1]))-1]=y
            i+=1
        j=0
        while(j<(len(arr2))):
                if((j+1)==len(arr2)):
                    z=z+arr2[j]
                else:    
                    z=z+arr2[j]+" "
                j+=1
        return z
