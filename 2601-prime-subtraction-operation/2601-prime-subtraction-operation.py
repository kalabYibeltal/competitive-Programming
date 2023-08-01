class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        primes = []
        for i in range(2,1000):
            primes.append(i)
            for j in range(2,i):
                if i%j == 0:
                    primes.pop()
                    break
        
        for index in range(len(nums)):
            # print(nums)
            if index > 0 and nums[index] <= nums[index - 1]:
                return 
            dec = 0
            p = 0
            # print(index)
            while primes[p] < nums[index] and (index == 0 or (index !=0 and nums[index] - primes[p] > nums[index-1])):
                
                dec = primes[p]
                p += 1
                if p == len(primes):
                    break
                # print(p, primes[p])
            
            nums[index] -= dec
            # print(nums)
        return True
    
    
    