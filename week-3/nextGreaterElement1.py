class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        i=0
        dictr={}
        arr=[]
        while i<len(nums2)-1:
            dictr[nums2[i]]=nums2[i+1]
            i+=1
        dictr[nums2[-1]]=nums2[-1]-1
        print(dictr)
        i=0
        while i<len(nums1):
            w=len(arr)
            j=0
            while j<len(nums2):
                if nums2[j]==nums1[i]:
                    k=j+1
                    n=nums2[j]
                    break
                else:
                    j+=1
            while k<len(nums2):
               
                if nums2[k]>n:
                 
                    arr.append(nums2[k])
                    break
                else:
                    k+=1
            if w==len(arr):
                arr.append(-1)
            i+=1
        return arr
