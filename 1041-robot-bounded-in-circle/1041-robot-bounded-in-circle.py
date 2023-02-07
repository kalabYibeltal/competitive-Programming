class Solution:    
    def isRobotBounded(self, instructions: str) -> bool:
        cord = [0, 0]
        vector = [[0, 1], [-1, 0], [0, -1], [1, 0]]
        index = 0
        for ins in instructions:
            if ins == "G":
                cord = [a + b for a, b in zip(cord, vector[index])]
            elif ins == "L":
                index = (index + 1) % 4
            elif ins == "R":
                index = (index - 1) % 4
        return cord == [0, 0] or index != 0