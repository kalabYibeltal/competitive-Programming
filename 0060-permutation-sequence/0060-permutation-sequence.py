class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        arr = list(range(1,n+1))
        num = ""
        size = math.factorial(n)    
        for i in range(1,n+1):
            h = size / len(arr)
            no = int(-1 * (-k // h))
            num += str(arr[no-1])
            arr.pop(no-1)
            
            k = k % h
            size = h
        
        return num
       
            