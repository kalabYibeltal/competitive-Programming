
def runningMedian(a):
    # Write your code here
    minh=[]
    maxh=[]
    arr=[]
    maxh.append(-a[0])
    heapq.heapify(maxh)
    heapq.heapify(minh)
    arr.append(a[0])
    i=1
    while i < len(a):
        if len(minh)==0:
            if a[i]>(-maxh[0]):
                heapq.heappush(minh,a[i])
                if(len(minh)>len(maxh)):
                    arr.append(minh[0])
                elif len(maxh)>len(minh):
                    arr.append(-maxh[0])
                else:
                    arr.append((minh[0]-maxh[0])/2)
            else:
                heapq.heappush(maxh,-a[i])
                x=-heapq.heappop(maxh)
                heapq.heappush(minh,x)
                
                if(len(minh)>len(maxh)):
                    arr.append(minh[0])
                elif len(maxh)>len(minh):
                    arr.append((-maxh[0]))
                else:
                    arr.append((minh[0]-maxh[0])/2)
            print(minh)
        elif a[i] > -maxh[0]:
            if len(maxh) < len(minh):
                # print(minh)
                heapq.heappush(minh,a[i])
                x=heapq.heappop(minh)
                # print(minh)
                heapq.heappush(maxh,-x)
                
                if(len(minh)>len(maxh)):
                    arr.append(minh[0])
                elif len(maxh)>len(minh):
                    arr.append((-maxh[0]))
                else:
                    arr.append((minh[0]-maxh[0])/2)
                # print(maxh)
                # print(minh)
                # print(arr)
            else:
                heapq.heappush(minh,a[i])
                if(len(minh)>len(maxh)):
                    arr.append(minh[0])
                elif len(maxh)>len(minh):
                    arr.append((-maxh[0]))
                else:
                    arr.append((minh[0]-maxh[0])/2)
            
        else:
            if len(maxh) > len(minh):
                x=-heapq.heappop(maxh)
                heapq.heappush(minh,x)
                heapq.heappush(maxh,-a[i])
                if(len(minh)>len(maxh)):
                    arr.append(minh[0])
                elif len(maxh)>len(minh):
                    arr.append((-maxh[0]))
                else:
                    arr.append((minh[0]-maxh[0])/2)
            else:
                heapq.heappush(maxh,-a[i])
                if(len(minh)>len(maxh)):
                    arr.append(minh[0])
                elif len(maxh)>len(minh):
                    arr.append((-maxh[0]))
                else:
                    arr.append((minh[0]-maxh[0])/2)
        i+=1
    return arr
        
       
        
