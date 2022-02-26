class Solution:
    #Heapify function to maintain heap property.

    def heapify(self,arr,a, n, i):
        
        # code here
        n=len(a)
        if 2*i+2<n:
            if a[2*i+1]<a[2*i+2] and a[i]>min(a[2*i+1],a[2*i+2]):
                a[i],a[2*i+1]=a[2*i+1],a[i]
            elif a[i]>min(a[2*i+1],a[2*i+2]):
                a[i],a[2*i+2]=a[2*i+2],a[i]
        elif 2*i+1<n and a[i]>a[2*i+1]: 
           a[i],a[2*i+1]=a[2*i+1],a[i]
    #Function to build a Heap from array.
    def build(self,arr,i):
        n=len(arr)
        if 2*i+2<n:
            if arr[2*i+1]<arr[2*i+2] and arr[i]>min(arr[2*i+1],arr[2*i+2]):
                arr[i],arr[2*i+1]=arr[2*i+1],arr[i]
                i=2*i+1
                self.build(arr,i)
            elif arr[i]>min(arr[2*i+1],arr[2*i+2]):
                arr[i],arr[2*i+2]=arr[2*i+2],arr[i]
                i=2*i+2
                self.build(arr,i)
        elif 2*i+1<n and arr[i]>arr[2*i+1]: 
           arr[i],arr[2*i+1]=arr[2*i+1],arr[i]
           i=2*i+1
           self.build(arr,i)
    
    def buildHeap(self,arr,n):
        # code here
        n=len(arr)
        i=n-2
        a=[]
        n=len(arr)
        a.append(arr.pop())
        while len(arr)>0:
            a.append(arr.pop())
            i=len(a)-1
            while((i-1)//2>=0):
                if a[i]<a[(i-1)//2]:
                    self.heapify(arr,a,n,(i-1)//2)
                    i=(i-1)//2
                else:
                    break
        return a
        # i=0
        # b=False
        # n=len(arr)
        # while i<n:
        #     b=False
        #     if 2*i+2<n and arr[i]>min(arr[2*i+1],arr[2*i+2]):
        #         self.heapify(arr,n,i)
        #         b=True
        #     elif 2*i+1<n and arr[i]>arr[2*i+1]:
        #         self.heapify(arr,n,i)
        #         b=True
        #     if b==True and (i-1)//2>=0 and arr[i]>arr[(i-1)//2] :
        #         self.heapify(arr,n,(i-1)//2)
        #     i+=1
            
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        ar=[]
        i=0
        arr=self.buildHeap(arr,n-1)
        while i<n:
            arr[0],arr[-1]=arr[-1],arr[0]
            ar.append(arr.pop())
            self.build(arr,0)
            i+=1
        
        i=0
        while i<len(ar):
            # arr.append(ar[i])
            print(ar[i], end=" ")
            i+=1
