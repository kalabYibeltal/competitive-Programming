class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        out = [0] * 100001
        ends = set()
        for x, y, val in segments:
            out[x] += val
            out[y] -= val
            ends.add(y)
        look = "start"
        start= 0 
        
        old = 0
        prefix = 0
        
        result = []
        # print(out)
        for i in range(1,len(out)):
            prefix += out[i]
            if prefix != old or i in ends:
                if look == "start":
                    start = i
                    look = "end"
                else:
                    result.append([start, i, old])
                    look = "start"
                    if prefix > 0:
                        start = i
                        look = "end"
            
            old = prefix
        
        return result
        