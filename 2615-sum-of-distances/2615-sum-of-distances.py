class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        pos = defaultdict(list)
        
        for index, num in enumerate(nums):
            pos[num].append(index)
        
        sol = [0] * len(nums)
        
        print(pos)
        for key in pos:
            value = 0
            for index in pos[key]:
                value += (index-pos[key][0])
            
            sol[pos[key][0]] = value
            
            
            for i in range(1, len(pos[key])):
                value += (i* (pos[key][i] - pos[key][i-1]))
                value -= ((len(pos[key]) - i)* (pos[key][i] - pos[key][i-1]))
                sol[pos[key][i]] = value
        
        return sol
                
                
                
                