class MedianFinder:
#     my first HARD level question by leetcode
    def __init__(self):
        self.minh=[]
        self.maxh=[]
    def addNum(self, num: int) -> None:
        if len(self.maxh)==0:
            self.maxh.append(-num) 
        elif len(self.minh)==0:
          
            if num >= (-self.maxh[0]):
                heapq.heappush(self.minh,num)
            else:
                x=-heapq.heappop(self.maxh)
                heapq.heappush(self.minh,x)
                heapq.heappush(self.maxh,-num)
        elif num < self.minh[0]:
            if len(self.maxh) > len(self.minh):
                heapq.heappush(self.maxh,-num)
                x=-heapq.heappop(self.maxh)
                heapq.heappush(self.minh,x)
                
            else:
                heapq.heappush(self.maxh,-num)
        else:
            if len(self.maxh) < len(self.minh):
                heapq.heappush(self.minh,num)
                x=heapq.heappop(self.minh)
                heapq.heappush(self.maxh,-x)
                
            else:
                heapq.heappush(self.minh,num)
            

    def findMedian(self) -> float:
        if(len(self.minh)>len(self.maxh)):
            return self.minh[0]
        elif len(self.maxh)>len(self.minh):
            return (-self.maxh[0])
        else:
            return (self.minh[0]-self.maxh[0])/2




# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
