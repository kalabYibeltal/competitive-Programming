import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        i=0
        while i<len(stones):
            stones[i]=-stones[i]
            i+=1
        
        heapq.heapify(stones)
        while len(stones)>1:
            
            x=-heapq.heappop(stones)

            y=-heapq.heappop(stones)
            if x>y:
                heapq.heappush(stones,y-x)

        if len(stones)==0:
            return 0
        else: return -stones[0]
