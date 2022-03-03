# counter=0
# ps=[]
# def dfs(con,node,tup):
#     for i in con[node]:
#         if i==1
def mark(isConnected,node,visited):
    # print(node)
    visited[node]=1
    # print(visited)
    j=0
    while j < len(isConnected[0]):
        if isConnected[node][j]==1 and node!=j and visited[j]==0:
            mark(isConnected,j,visited)
        j+=1
    


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited =[0]*len(isConnected)
        count=0
        x=0
        i=0
        while i < len(isConnected):
            if visited[i]==1:
                i+=1
            else:
                visited[i]=1
                count+=1
                j=0
                while j < len(isConnected[0]):
                    if isConnected[i][j]==1 and i!=j and visited[j]==0:
                        print(j)
                        mark(isConnected,j,visited)
                    j+=1
                i+=1
        return count
       
