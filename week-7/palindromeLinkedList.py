# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         h=head
#         while h:
#             x=h
#             h=h.next
#         a=head
#         b=a.next
#         while a:
#             m=b
#             b=a.next
#             a.next=m
#             c=b.next
#             b.next=a
#             a=c
#         print(x.val)
     
        
        
        h=head
        b=True
        arr=[]
        while h:
            arr.append(h.val)
            h=h.next
        h=head
        x=len(arr)-1
        while h:
            if not(h.val==arr[x]):
                b=False
            x-=1
            h=h.next
        return b
