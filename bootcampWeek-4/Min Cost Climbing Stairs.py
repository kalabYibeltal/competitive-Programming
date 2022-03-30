class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # cost.append(0)
        dictr = {}
        def costs(i):
            if i >= len(cost):
                return inf
            if i in dictr:
                return dictr[i]
            if i == len(cost)-1 or i==len(cost)-2:
                dictr [i] = cost[i]
                return cost[i]
            else:
                if i == -1:
                    val = min(costs(i+1),costs(i+2)) 
                    return val
                val = min(costs(i+1),costs(i+2)) + cost[i]
                dictr[i] = val 
                return val
        return costs(-1)
   
