class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        heapmn = []
        heapmx = []
        for i in range(len(weights)-1):
            heappush(heapmn,weights[i]+weights[i+1])
            heappush(heapmx,-(weights[i]+weights[i+1]))
        
        ans = 0
        for j in range(k-1):
            ans += (-heappop(heapmx) - heappop(heapmn))
        
        return ans