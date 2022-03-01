"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
def idFinder(id, employees):
    for l in employees:
        if l.id == id:
            return l
        
def subs(i: 'Employee', employees):
    sum=0
    for j in i.subordinates:
        sum+=subs(idFinder(j,employees),employees)
        
    return sum + i.importance
    
    
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        for l in employees:
            if l.id == id:
                return subs(l,employees)
               
                
            
# another implmentation            
# def subs(i: 'Employee', dictr):
#     sum=0
#     for j in i.subordinates:
#         sum+=subs(dictr[j],dictr)     
#     return sum + i.importance
       
# class Solution:
#     def getImportance(self, employees: List['Employee'], id: int) -> int:
#         dictr={}
#         for l in employees:
#             dictr[l.id]=l
#         return subs(dictr[id],dictr)
               
                     
                
