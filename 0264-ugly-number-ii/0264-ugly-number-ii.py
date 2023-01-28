class Solution:
    def nthUglyNumber(self, n: int) -> int:
        k = [0] * n
        t1 = t2 = t3 = 0
        k[0] = 1
        for i in range(1,n):
            k[i] = min(k[t1]*2,k[t2]*3,k[t3]*5)
            if(k[i] == k[t1]*2): t1 += 1
            if(k[i] == k[t2]*3): t2 += 1
            if(k[i] == k[t3]*5): t3 += 1
    
        
        # print(k)
        return k[n-1]
    
    
        heap = [1]
        visited = set()
        count = 0
        while heap:
            num = heappop(heap)
            count += 1
            if count == n: 
                return num
            for i in [2,3,5]:
                if num * i not in visited:
                    visited.add(num * i)
                    heappush(heap,num * i)
            
        