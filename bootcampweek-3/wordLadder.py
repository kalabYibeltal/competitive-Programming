import collections
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        # print(len(wordList))
        def plusplus(oldChar):
            return chr(ord(oldChar)+1)
        plusplus('a') # output - b
        words={}
        dictr={}
        for i in wordList:
            words[i]=1
        for i in wordList:
            dictr[i]=[]
        
        
        for word in dictr:
            main=word
            i=0
            while i < len(word):
                
                j=0
                while j < 26:
                    k=0
                    t=""
                    while k < len(word):
                        if k==i:
                            # print(k)
                            t+=(chr(ord('a')+j))
                        else: t+=main[k]
                        k+=1
                    word=t
     
                    if word in words:
                        
                        dictr[main].append(word)
                  
                
                    j+=1
                i+=1
                
                
# cleaner code with bigger time complexity
#         def match(word1,word2):
#             i=0
#             e=0
#             while i < len(word1):
#                 if word1[i]!=word2[i]:
#                     e+=1
#                 if e>1:
#                     return False
#                 i+=1
#             return True
        
#         dictr={}
#         for i in wordList:
#             dictr[i]=[]
            
#         for i in dictr:
#             for j in wordList:
#                 if match(i,j):
#                     dictr[i].append(j)
#         # 

        # print(dictr)
        
        que=collections.deque([beginWord])
        level=collections.deque([1])
        visited=set()
        visited.add(beginWord)
        while que:
            cur=que.popleft()
            lev=level.popleft()
            if cur==endWord: return lev
            for i in dictr[cur]:
                if i not in visited:
                    visited.add(i)
                    que.append(i)
                    level.append(lev+1)
        return 0
                
                
    
