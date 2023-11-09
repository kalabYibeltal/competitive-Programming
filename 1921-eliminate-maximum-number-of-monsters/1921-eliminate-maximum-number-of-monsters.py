class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        heap = []
        for i in range(len(dist)):
            heap.append( (dist[i] // speed[i]) if (dist[i] % speed[i] == 0) else (dist[i] // speed[i]) + 1 )
        
        heap.sort()
        # print(heap)
        
        for t in range(len(heap)):
            
            if t >= heap[t]:
                return t
        
        return len(heap)