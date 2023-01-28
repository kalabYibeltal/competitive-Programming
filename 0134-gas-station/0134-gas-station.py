class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        #from neetcode
        if sum(gas) < sum(cost):
            return -1
        
        
        start = 0
        tank = 0
        for i in range(len(gas)):
            tank += (gas[i] - cost[i])
            if tank < 0:
                tank = 0
                start = i + 1
        
        return start
    
    
        #my beautifull 
        if sum(cost) > sum(gas): return -1
        if len(cost) == 1: return 0
        arr = []
        for i in range(len(gas)):
            arr.append(gas[i] - cost[i])
                
        index = 0
        while index < len(arr):
            if arr[index] > 0:
                total = arr[index]
                temp = index
                index += 1
                test = True
                while index < len(arr):
                    total += arr[index]
                    if total < 0:
                        test = False
                        break
                    index += 1
                
                if test:
                    return temp

            index += 1        
  