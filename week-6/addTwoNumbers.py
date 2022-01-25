# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1=0
        x=1
        while(l1):
            num1=num1+x*(l1.val)
            l1=l1.next
            x=x*10
        num2=0
        print(num1)
        x=1
        while(l2):
            num2=num2+x*(l2.val)
            l2=l2.next
            x=x*10
        sum1=num1+num2
        print(sum1)
        s=str(sum1)
        l3=ListNode()
        print(l3.val)
        y=l3
        i=len(s)-1
        while(i>-1):
            y.next=ListNode(int(s[i]))
            y=y.next
            i=i-1
        print(y.val)
        return l3.next
    
            
