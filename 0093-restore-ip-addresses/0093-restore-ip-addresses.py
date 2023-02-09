class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ip = s
        ans = []
        def back(i,path,count):
            if count == 4: 
                return 
            if i == len(ip) and count == 3:
                ans.append(path)
                return
            if i == len(ip): return 

            if len(path) == 0:
                back(i+1,path+ip[i],count)
            elif len(path) >= 1 and path[-1] == "0" and (len(path)==1 or path[-2]=="."):
                back(i+1,path + "."+ ip[i],count+1)

            elif len(path) == 1 or  (len(path) >= 2 and path[-2] == "."):
                back(i+1,path+ip[i],count)
                back(i+1,path + "."+ ip[i],count+1)

            elif len(path) == 2 or (len(path) >= 3 and path[-3] == "."):
                s = path[len(path)-2:]
                if int(s + ip[i]) <= 255:
                    back(i+1,path+ip[i],count)
                back(i+1,path + "."+ ip[i],count+1)

            elif len(path) == 3 or (len(path) >= 4 and path[-4] == "."):
                s = path[len(path)-3:]
                if int(s) > 255: return 
                back(i+1,path + "."+ ip[i],count+1)
        

        back(0,"",0)
        return ans