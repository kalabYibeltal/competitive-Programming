class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        dirr = [[0,1],[0,-1],[1,0],[1,1],[1,-1],[-1,1],[-1,0],[-1,-1]]
        out = []
        queen = set()
        for x, y in queens:
            queen.add((x,y))
        # queens = set(queens)
        for dx,dy in dirr:
            tempx, tempy = king
            while True:
                if 0 <= tempx + dx < 8 and 0 <= tempy + dy < 8:
                    tempx += dx
                    tempy += dy
                    if (tempx,tempy) in queen:
                        out.append([tempx,tempy])
                        break
                else:
                    break
        
        return out