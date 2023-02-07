class Solution:
    def minOperations(self, logs: List[str]) -> int:
      
        opps = 0
        
        for log in logs:
            if log != "../" and log != "./": opps += 1
            elif log == "../" and opps != 0: opps -= 1
        return opps
        