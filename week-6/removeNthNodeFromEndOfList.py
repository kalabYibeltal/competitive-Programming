# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count=0
        h=head
        p=head
        while(h):
            h=h.next
            count+=1
        x=count-n
        
        i=0
        h=head
        print(x)
        if (x==0):
            head=head.next
            return head
        
      
        while(i<x):
            p=h
            h=h.next
            i=i+1
        p.next=h.next
    
        return head
        
