import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.n=nums
        self.k=k
        heapq.heapify(self.n)
        j=0
        
        if k<len(self.n):
           
            x=len(self.n)
            while j < (x-k):
              
                heapq.heappop(self.n)
                j+=1
        print(self.n)
    def add(self, val: int) -> int:
        if len(self.n)==0 or len(self.n)<self.k:
            heapq.heappush(self.n,val)
   
        elif val > self.n[0]:
            heapq.heappop(self.n)
        
            heapq.heappush(self.n,val)
            
        return self.n[0]
        

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
