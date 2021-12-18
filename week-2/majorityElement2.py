class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        x=n/3
        i=0
        arr=set()
        arr2=[]
        dictr={}
        if(x<1):
            if(len(nums)==1):
                arr.add(nums[0])
            else:
                arr.add(nums[0])
                arr.add(nums[1])
            return arr
        else:
            while(i<n):
                y=len(arr)
                arr.add(nums[i])
                if(len(arr)==y):

                    if nums[i] in dictr:
                        dictr[nums[i]] += 1
                    else:
                        dictr[nums[i]] = 2
                i+=1
            for c in dictr:
                if(dictr[c]>x):
                    arr2.append(c)
        return arr2
