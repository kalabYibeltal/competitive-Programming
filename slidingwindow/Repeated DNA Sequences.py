class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dna = set()
        ans = []
        ansr = set()
        for r in range(10,len(s)+1):
            if s[r-10:r] in dna and s[r-10:r] not in ansr: 
                ans.append(s[r-10:r])
                ansr.add(s[r-10:r])
            else: dna.add(s[r-10:r])
        
        return ans
