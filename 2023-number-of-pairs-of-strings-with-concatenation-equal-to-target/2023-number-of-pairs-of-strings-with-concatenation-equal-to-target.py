class Solution:
    def numOfPairs(self, nums: List[str], t: str) -> int:
        res = 0
        for i in nums:
            x=nums.copy()
            p = t
            if i==p[:len(i)]:
                p=p[len(i):]
                x.remove(i)
                res+=x.count(p)
        return res 