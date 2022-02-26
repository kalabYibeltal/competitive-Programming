import heapq
n = int(input())

i=0
nums=[]
dictr={}
while i<n:
    y = input()
    arr= y.split()
    z=int(arr[0])
    
    if z==1:
        heapq.heappush(nums,int(arr[1]))
        if nums[0] in dictr and dictr[nums[0]] > 0 :
            dictr[nums[0]]-=1
            heapq.heappop(nums)
            
    elif z==2:
        if int(arr[1]) in dictr:
            dictr[int(arr[1])]+=1
        else:
            dictr[int(arr[1])]=1
        if nums[0] in dictr and dictr[nums[0]] > 0 :
            dictr[nums[0]]-=1
            heapq.heappop(nums)
            
    elif z==3:
        while nums[0] in dictr and dictr[nums[0]] > 0 :
            dictr[nums[0]]-=1
            heapq.heappop(nums)
            
        print(nums[0])
    i+=1     
    
