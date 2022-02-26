def cookies(k, A):
    # Write your code here
  
    heapq.heapify(A)
    i=0
    while A[0]<k and len(A)>=2 :
        i+=1
        x=heapq.heappop(A)
        y=heapq.heappop(A)
        heapq.heappush(A,x+2*y)
    if A[0]<k:
        return -1
    return i
