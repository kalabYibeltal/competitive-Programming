class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = [[-a,"a"],[-b,"b"],[-c,"c"]]
        heapify(heap)
        string = ""
        while True:
            val, let = heappop(heap)
            if val < 0 and (len(string) < 2 or not( string[-1] == string[-2] == let)):
                string += let
                heappush(heap,[val+1,let])
            elif val == 0:
                return string
            else:
                val2, let2 = heappop(heap)
                if val2 == 0:
                    return string
                string += let2
                heappush(heap,[val2+1,let2])
                heappush(heap,[val,let])
                
            