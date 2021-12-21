class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        j=0
        n=len(intervals)
        arr=[]
        intervals.sort()
        j=n-1
        print(intervals)
        if len(intervals)==1:
                return intervals
        while(j>0):
            if intervals[j][0]<=intervals[j-1][1]:
                x=intervals[j-1][0]
                y=max(intervals[j-1][1],intervals[j][1])
                intervals.pop(-1)
                intervals.pop(-1)
                intervals.append([x,y])
                if len(arr)>0:
                    while arr[-1][0]<=intervals[j-1][1]:
                        intervals.append(arr.pop(-1))
                        x=intervals[j-1][0]
                        y=max(intervals[j-1][1],intervals[j][1])
                        intervals.pop(-1)
                        intervals.pop(-1)
                        intervals.append([x,y])
                        if len(arr)==0:
                            break
                if len(intervals)==1:
                    break
            else:
                arr.append(intervals.pop(-1))
                if len(intervals)==1:
                    break 
            
            j=len(intervals)-1
                
                 
        return intervals+arr
