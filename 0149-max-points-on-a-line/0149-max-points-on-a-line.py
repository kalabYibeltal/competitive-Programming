class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        lines = defaultdict(list)
        output = 0
        for p1 in range(len(points)):
            for p2 in range(p1 +1, len(points)):
                if points[p1][0] == points[p2][0]:
                    slope = 0.123456789
                else:
                    slope = (points[p1][1] - points[p2][1]) / (points[p1][0] - points[p2][0])
                
                
                lines[p1].append(slope)
   
            if lines[p1]:
                output = max(output, sorted(Counter(lines[p1]).values())[-1] )
        
        return output + 1
       