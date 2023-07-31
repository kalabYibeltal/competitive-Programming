class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        heap = []
        total = 0
        visited = set()
        var = []
        for i in range(len(mat)):
            var.append((0,i))
            total += mat[i][0]
            
        
        t = tuple([total] + var)
        visited.add(t)
        heappush(heap, t)
        
        for i in range(k):
            tup = heappop(heap)
            array = list(tup)
            # print(array)
            if i == k - 1:
                return array[0]
            
            
            
            for i in range(1, len(array)):
                if array[i][0] == len(mat[0]) - 1:
                    continue
                newarray = array.copy()
                
                # print(newarray)
                newarray[0] += mat[newarray[i][1]][newarray[i][0] + 1] - mat[newarray[i][1]][newarray[i][0]]
                newarray[i] = (newarray[i][0] +1, newarray[i][1] )

                t = tuple(newarray)
                if t not in visited:
                    visited.add(t)
                    heappush(heap,t)
                
                
                
                
                