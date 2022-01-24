# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        value=head
        middle=head
        count=0
        while(value.next):
            if(count%2==0):
                middle=middle.next
                count+=1
                value=value.next
            else:
                count+=1
                value=value.next
        return middle
