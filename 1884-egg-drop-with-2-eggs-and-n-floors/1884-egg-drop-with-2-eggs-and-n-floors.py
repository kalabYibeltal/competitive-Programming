class Solution:
    def twoEggDrop(self, n: int) -> int:
        if n < 3:
            return n
        arr = []
        curr = 1
        while n > 0:
            arr.append(n)
            n = n - curr
            curr += 1
        
        return arr[-2] - arr[-1] + 1 
    
      