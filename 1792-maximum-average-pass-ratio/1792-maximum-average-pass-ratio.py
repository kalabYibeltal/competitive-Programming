class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = []
        for upper, lower in classes:
            heappush(heap, [-(((upper + 1)/(lower + 1)) - (upper/lower)), upper, lower])
        
        for i in range(extraStudents):
            adder , upper , lower = heappop(heap)
            heappush(heap, [-(((upper + 2)/(lower + 2)) - ((upper + 1)/(lower + 1))), upper+1, lower+1])
        
        total = sum([upper/lower for adder,upper,lower in heap])
        return total/len(classes)
            
            
            