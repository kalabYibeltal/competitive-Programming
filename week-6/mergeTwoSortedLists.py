# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l3=ListNode()
        l4=l3
        while(list1 and list2):
            if list1.val<=list2.val:
                new=ListNode()
                new.val=list1.val
                l3.next=new
                l3=l3.next
                list1=list1.next
            else:
                new=ListNode()
                new.val=list2.val
                l3.next=new
                l3=l3.next
                list2=list2.next
        if list1:
            while list1:
                new=ListNode()
                new.val=list1.val
                l3.next=new
                l3=l3.next
                list1=list1.next
                l3.next=None
        elif list2:
            while list2:
                new=ListNode()
                new.val=list2.val
                l3.next=new
                l3=l3.next
                list2=list2.next
                l3.next=None
        return l4.next
