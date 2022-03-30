class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) == 2 and nums[0] == nums[1]:
            return 1
        i=0
        evendic={}
        odddic={}
        while i < len(nums):
            if i%2==0:
                if nums[i] in evendic:
                    evendic[nums[i]]+=1
                else:
                    evendic[nums[i]]=1
            elif i%2!=0:
                if nums[i] in odddic:
                    odddic[nums[i]]+=1
                else:
                    odddic[nums[i]]=1
            i+=1
        print(evendic, odddic)
        maxe=0
        maxe2=0
        maxen = nums[0]
        maxen2 = nums[0]
        for n in evendic:
            if evendic[n] > maxe:
                maxe2 = maxe
                maxe = evendic[n]
                maxen2 = maxen
                maxen = n
            elif evendic[n] > maxe2:
                maxe2 = evendic[n]
                maxen2 = n
                
        maxo=0
        maxo=0
        maxon= nums[0]
        maxon2 = nums[0]
       
        for n in odddic:
            if odddic[n] > maxo:
                maxo2 = maxo
                maxo = odddic[n]
                maxon2 = maxon
                maxon = n
            elif odddic[n] > maxo2:
                maxo2 = odddic[n]
                maxon2 = n
        if maxen == maxon and maxen2 != maxen and ((maxe <= maxo and maxe2 >= maxo2) or (maxe2 >=  maxo and maxo!=maxo2)):
            maxen = maxen2
        elif maxen == maxon and maxon2 != maxon:
            maxon = maxon2
        elif maxon == maxen:
            return len(nums)//2
        count=0
        i = 0
        while i < len(nums):
            if i%2==0 and nums[i]!= maxen:
                count+=1
            elif i%2 != 0 and nums[i] != maxon:
                count+=1
            i+=1
        return count
                
            
            
            
            
