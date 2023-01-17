class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        out = []
        test = True
        for x, y in intervals:
            if y < newInterval[0] or x > newInterval[1]:
                if out and x <= out[-1][1]:
                    out[-1][1] = max(y, out[-1][1])
                else:
                    out.append([x,y])
            else:
                if out and x <= out[-1][1]:
                    out[-1][1] = max(y, out[-1][1])
                else:
                    test = False
                    out.append([min(x, newInterval[0]), max(y, newInterval[1])])
            
        if test: out.append(newInterval) 
        out.sort()
        return out
                