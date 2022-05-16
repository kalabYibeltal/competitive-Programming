class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        minn = inf
        for i in range(len(timePoints)):
            h = int(timePoints[i][0:2])
            m = int(timePoints[i][3:5])
            if i == len(timePoints) - 1: 
                h2 = int(timePoints[0][0:2]) + 24
                m2 = int(timePoints[0][3:5])
            else:
                h2 = int(timePoints[i+1][0:2])
                m2 = int(timePoints[i+1][3:5])

            dif = (h2*60+m2)-(h*60+m)
            minn = min(minn,dif)
            
        return minn
