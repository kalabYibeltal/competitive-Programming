class Solution(object):
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits = []
        strings = []
        
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                strings.append(log)
            
                
        strings.sort(key = lambda x:(x.split()[1:], x.split()[0])) 
        
        return strings + digits