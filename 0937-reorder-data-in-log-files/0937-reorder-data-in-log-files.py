class Solution(object):
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digitLogs = []
        letterLogs = []
        
        for log in logs:
            digit = True if log.split()[1].isdigit() else False
            
            if digit:
                digitLogs.append(log)
            else:
                letterLogs.append(log)
            
                
        letterLogs.sort(key = lambda x:(x.split()[1:], x.split()[0])) 
        
        return letterLogs+digitLogs