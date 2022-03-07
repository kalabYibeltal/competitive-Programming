# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

head = ListNode()
head.next=L
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr=[]
        i=0
        if len(lists)==0 :
            return 
        while i < len(lists):
            node=lists[i]
            while node:
                arr.append(node.val)
                node=node.next
            i+=1
        arr.sort()
        if len(arr)==0:
            return
        i=0
        node=ListNode()
        head=node
        while i < len(arr):
            node.val=arr[i]
            if i!=len(arr)-1:
                node.next=ListNode()
                node=node.next
            i=i+1
        return head
