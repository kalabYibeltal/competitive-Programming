class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = []
        for let, value in Counter(s).items():
            heappush(heap, [-value, let])
        answer = ""
        while heap:
            value , let = heappop(heap)
            if len(answer) > 0 and let == answer[-1]:
                if not heap:
                    return ""
                value2, let2 = heappop(heap)
                answer += let2
                if value2 != -1:
                    heappush(heap, [value2 + 1, let2])
                heappush(heap, [value, let])
            else:
                answer += let
                if value != -1:
                    heappush(heap, [value + 1, let])
            
        return answer
                
