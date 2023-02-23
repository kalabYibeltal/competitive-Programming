
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        cordx = [(rec1[0],rec1[2]),(rec2[0],rec2[2])]
        cordy = [(rec1[1],rec1[3]),(rec2[1],rec2[3])]
        cordx.sort()
        cordy.sort()
        if cordx[1][0]<cordx[0][1] and cordy[1][0]<cordy[0][1]:
            return True
        return False