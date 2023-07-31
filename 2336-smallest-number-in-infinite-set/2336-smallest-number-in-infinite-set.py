class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        self.index = 1
        self.visited = set()
        
    def popSmallest(self) -> int:
        if self.heap:
            self.visited.remove(self.heap[0])
            return heappop(self.heap)
        
        self.index += 1
        return self.index-1
            

    def addBack(self, num: int) -> None:
        if num < self.index and num not in self.visited:
            self.visited.add(num)
            heappush(self.heap,num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)