class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        tot = sum(nums)

        l, r = nums[:n//2], nums[n//2:]
        lsum, rsum = defaultdict(set), defaultdict(set)

        for k in range(n // 2 + 1):
            lsum[k] |= set(map(sum, combinations(l, k)))
            rsum[k] |= set(map(sum, combinations(r, k)))
        
        
        ans = inf
        for k in lsum:
            rsum_cand = sorted(rsum[n // 2 - k])
            for ls in lsum[k]:
                cand = tot // 2 - ls                
                loc = bisect.bisect(rsum_cand, cand)
                if loc == 0:
                    rs = rsum_cand[loc]
                    ans = min(ans, abs(tot - 2 * (rs + ls)))
                elif loc == len(rsum_cand):
                    rs = rsum_cand[loc-1]
                    ans = min(ans, abs(tot - 2 * (rs + ls)))
                else:
                    rs1, rs2 = rsum_cand[loc-1], rsum_cand[loc]
                    ans = min(ans, abs(tot - 2 * (rs1 + ls)), abs(tot - 2 * (rs2 + ls)))        
        
        return ans