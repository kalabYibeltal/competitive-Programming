# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = ListNode()
        left.next = head
        
        right =  head
        prev = head
        answer = left
        
        
        while right:
            while left.next and left.next.val < x and left != right:
                left = left.next
                
            if right.val < x and right != left:
#                 if left.next == right:
#                     left.val, right.val = right.val, left.val
#                     prev = right
#                     right = right.next
                    
#                 else:
                temp1 = right
                right = right.next
                prev.next = right

                temp = left.next
                left.next = temp1
                temp1.next = temp
                left = temp1
            
            else:
                prev = right
                right = right.next
        
        return answer.next
        
                