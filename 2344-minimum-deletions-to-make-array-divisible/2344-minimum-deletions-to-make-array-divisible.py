class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        gcd = numsDivide[0] 
        def GCD(a,b):
            if b == 0: return a
            return GCD(b, a%b)
        
        for num in numsDivide:
            gcd = GCD(max(gcd,num), min(gcd,num))
        
        nums.sort()
        
        for i in range(len(nums)):
            if gcd % nums[i] == 0: return i
        
        return -1
            
            