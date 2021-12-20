class Solution:
    def isValid(self, s: str) -> bool:
        arr=[]
        boll=False
        for c in s:
            if(c=="[" or c=="(" or c=="{"):
                arr.append(c)
                boll=False
            elif(c=="]"):
                if(len(arr)==0):
                    return False
                elif(arr.pop()=="["):
                    boll=True
                else:
                    return False
            elif(c==")"):
                if(len(arr)==0):
                    return False
                elif(arr.pop()=="("):
                    boll=True
                else:
                    return False    
            elif(c=="}"):
                if(len(arr)==0):
                    return False
                elif(arr.pop()=="{"):
                    boll=True
                else:
                    return False
        if(len(arr)!=0):
            boll=False
        return boll
