from collections import defaultdict
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n=len(img1)
        d=defaultdict(int)
        maxc=0
        for x1 in range(n):
            for y1 in range(n):
                if img1[x1][y1]==1:
                    for x2 in range(n):
                        for y2 in range(n):
                            if img2[x2][y2]==1:
                                diff=((x2-x1),(y2-y1))                    
                                d[diff]+=1
                                maxc=max(maxc,d[diff])
        #print(d)
        return maxc