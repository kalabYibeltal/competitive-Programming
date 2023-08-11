class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq = Counter(s)
        heap = []
        for key, val in freq.items():
            heappush(heap, [-(ord(key) - ord("a")), -val])
        
        answer = ""
        counter = 0
        while heap:
            let, count = heappop(heap)
            if answer and chr((let * -1) + ord("a")) == answer[-1]:
                if counter + 1 > repeatLimit:
                    if not heap: return answer
                    let2, count2 = heappop(heap)
                    if count2 == 0:
                        return answer
                    answer += chr((let2 * -1) + ord("a"))
                    counter = 1
                    if count2 + 1 < 0: heappush(heap, [let2, count2+1])
                    heappush(heap, [let, count ])
                    
                else:
                    answer += chr((let * -1) + ord("a"))
                    counter += 1
                    if count + 1 < 0: heappush(heap, [let, count+1])
            
            else:
                answer += chr((let * -1) + ord("a"))
                counter = 1
                if count + 1 < 0: heappush(heap, [let, count+1])

                    
        return answer