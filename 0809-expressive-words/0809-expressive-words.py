class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        
        res = 0
        s_chars, s_counts = self.process(s)
        for word in words:
            w_chars, w_counts = self.process(word)
            
            if s_chars != w_chars:
                break

            can_match = True
            for k in range(len(w_chars)):
                if not (w_counts[k] == s_counts[k] or (w_counts[k] < s_counts[k] and s_counts[k] >= 3)):
                    can_match = False
                    break
            if can_match:
                res += 1

        return res
    
    def process(self, strs):
        if not strs:
            return [], []
        chars, counts = [strs[0]], [1]

        for i in range(1, len(strs)):
            if strs[i] == chars[-1]:
                counts[-1] += 1
            else:
                chars.append(strs[i])
                counts.append(1)
        return chars, counts