class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        stickerCount = []
        for i, s in enumerate(stickers):
            stickerCount.append({})
            for c in s:
                stickerCount[i][c] = 1 + stickerCount[i].get(c, 0)
        
        dp = {}
        def dfs(t, stick):
            if t in dp:
                return dp[t]
            res = 1 if stick else 0
            remainT = ""
            for c in t:
                if c in stick and stick[c] > 0:
                    stick[c] -= 1
                else:
                    remainT += c
            used = float("inf")
            if remainT:
                for s in stickerCount:
                    if remainT[0] not in s:
                        continue
                    used = min(used, dfs(remainT, s.copy()))
                res += used
                dp[remainT] = used
            return res
                    
            
        res = dfs(target, {})
        return res if res != float("inf") else -1
        