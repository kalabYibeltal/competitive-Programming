import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        i=1
        x=words[0]
        arr=[]
        arr.append([-1,x])
        while i<len(words):
            if words[i]==x:
                arr[-1][0]-=1
            else:
                x=words[i]
                arr.append([-1,x])
            i+=1
        
        heapq.heapify(arr)
        print(arr)
        ar=[]
        i=0
        while i<k:
            x=heapq.heappop(arr)
            ar.append(x[1])
            i+=1
        return ar
    
    
    
#         word=Counter(words)
#         arr=[]
#         j=0
#         for i in word:
#             ar=[]
#             ar.append(word[i])
#             ar.append(i)
#             arr.append(ar)
#             j+=1
#             if j== k:
#                 break
#         arr.append([4,"ab"])
#         arr=sorted(arr, key=lambda x:-x[0], x[1])
#         print(arr)
#         return arr
                    
