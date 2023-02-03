class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.total = 0
        self.prefix_sum = []
        
        for weight in w:
            self.total += weight
            self.prefix_sum.append(self.total)
            

    def pickIndex(self) -> int:
        picked= random.randint(1, self.total)
        pickedI = bisect.bisect_left(self.prefix_sum, picked)
        return pickedI
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()