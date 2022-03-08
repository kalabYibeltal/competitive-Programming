import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap=[]
        for i in matrix:
            for j in i:
                if len(heap)<k:
                    heapq.heappush(heap,-j)
                elif j<-heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap,-j)
        return -heap[0]
