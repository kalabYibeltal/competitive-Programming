class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        firstp = 0
        secondp = 0
        
        ans = []
        while firstp < len(firstList) and secondp < len(secondList):
            if firstList[firstp][1] >= secondList[secondp][1]:
                if firstList[firstp][0] <= secondList[secondp][1]:
                    ans.append([max(firstList[firstp][0], secondList[secondp][0]), secondList[secondp][1]])
                
                secondp += 1
            
            else:
                if firstList[firstp][1] >= secondList[secondp][0]:
                    ans.append([max(firstList[firstp][0], secondList[secondp][0]), firstList[firstp][1] ])
                
                firstp += 1
            
        return ans