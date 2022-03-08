import heapq
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap=[]
        i=1
        if ladders==0:
            while i<len(heights):
                if 0<=heights[i]-heights[i-1] <= bricks:
                    
                    bricks=bricks-(heights[i]-heights[i-1])
                    i+=1
                elif heights[i]-heights[i-1] < 0:
                    i+=1
                else:
                    break
            return i-1
                
                
        while i<len(heights):
            # print([heap,bricks]) 
            if len(heap)<ladders:
                heapq.heappush(heap,[heights[i]-heights[i-1],i])
                i+=1
              
            elif (heights[i]-heights[i-1]) > heap[0][0]  and heap[0][0] <= bricks:
                x=heapq.heappop(heap)
                heapq.heappush(heap,[heights[i]-heights[i-1],i])
                if x[0]>0:
                    bricks=bricks-x[0]
                i+=1
            elif 0<=(heights[i]-heights[i-1])<=bricks:
                bricks=bricks-(heights[i]-heights[i-1])
                i+=1
            elif (heights[i]-heights[i-1])<0:
                i+=1
            else:
                break
        return i-1
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
