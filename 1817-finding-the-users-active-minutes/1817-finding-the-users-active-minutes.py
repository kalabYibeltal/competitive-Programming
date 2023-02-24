class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        ans = set()
        for i in logs: ans.add(tuple(i))
        ans  = sorted(ans)
        dicr = defaultdict(int)
        for i in ans: dicr[i[0]] +=  1
        ret = [0] * k
        for i in dicr: ret[dicr[i]-1] += 1
        return ret
        