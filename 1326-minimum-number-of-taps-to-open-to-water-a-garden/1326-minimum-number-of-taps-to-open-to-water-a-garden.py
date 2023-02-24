class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        out = []
        for index, val in enumerate(ranges):
            if val != 0:
                out.append([max(0, index - ranges[index]), min(n, index + ranges[index])]) 
        
        out.sort()
        count = 0
        cur = 0
        p = 0
        if not out:
            return -1
        print(out)
        while cur < n:
            maxs = -1
            if p == len(out):
                break
            while out[p][0] <= cur:
                maxs = max(maxs, out[p][1])
                p += 1
                if p == len(out):
                    break

                
            cur = maxs
            if maxs == -1:
                return -1
            count += 1 
        
        if cur < n:
            return -1
        return count