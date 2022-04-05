class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        put = []
        visited = set()
        dirr = [[0,1],[1,0],[0,-1],[-1,0]]
        dp = 0
        i = [0,0]
        visited.add((i[0],i[1]))
        put.append(matrix[i[0]][i[1]])
        def valid(row,col): return 0<=row<len(matrix) and 0<=col< len(matrix[0])
        while len(put) < (len(matrix) * len(matrix[0])):
            if valid(i[0]+dirr[dp%4][0],i[1]+dirr[dp%4][1]) and (i[0]+dirr[dp%4][0],i[1]+dirr[dp%4][1]) not in visited:
                i[0] += dirr[dp%4][0]
                i[1] += dirr[dp%4][1]
                visited.add((i[0],i[1]))
                put.append(matrix[i[0]][i[1]])
            else:
                dp += 1
        return put
