class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0 
        c = 0
        ans = k
        for r in range(len(blocks)):
            if (r-l) < k:
                if blocks[r] == "W":
                    c += 1
            else:
                ans = min(c, ans)
                if blocks[l] == "W":
                    c -= 1
                l += 1
                if blocks[r] == "W":
                    c += 1
        
        ans = min(c, ans)
        return ans
                