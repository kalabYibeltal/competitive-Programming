from sortedcontainers import SortedList
class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        print(5 ^ 2 ^ 1 ^ 6)
        val = 0
        m = 0
        l = SortedList()
        arr = [0] * len(matrix[0])
        for i in range(len(matrix)):
            
            val = 0
            for j in range(len(matrix[0])):
                arr[j] = arr[j] ^ matrix[i][j]
                val = val ^ arr[j]
                
                # print(i,j,val)
                l.add(val)
           
           
        
        # print(l)
        return l[-k]
