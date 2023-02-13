class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        dic = {}
        dic[1] = [1]
        ans = 1
        for i in range(30):
            ans *= 2
            if len(str(ans)) in dic: dic[len(str(ans))].append(ans)
            else: dic[len(str(ans))] = [ans]
        
        for i in dic[len(str(n))]:
            if Counter(str(n)) == Counter(str(i)): return True
        return False
        
        