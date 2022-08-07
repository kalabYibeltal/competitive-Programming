class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dictr = {}
        def find(dep, let):
            if dep == n: return 1
            if (dep, let) in dictr: return dictr[(dep,let)]
            ans = 0
            # print(let,dep)
            if let == 'a': ans = find(dep + 1, 'e')
            elif let == 'e': ans = find(dep + 1, 'a') + find(dep+1, 'i')
            elif let == 'o': ans = find(dep + 1, 'u') + find(dep+1, 'i')
            elif let == 'u': ans = find(dep + 1, 'a') 
            else: ans = find(dep +1, 'a') + find(dep+1, 'e') + find(dep +1, 'u') + find(dep+1, 'o')
            dictr[(dep,let)] = ans
            return ans
        
        ans = find(1, 'a') + find(1, 'e') + find(1, 'i') + find(1, 'o') + find(1, 'u') 
        return ans % 1000000007
