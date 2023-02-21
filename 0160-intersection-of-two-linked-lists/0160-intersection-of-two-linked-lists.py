class Solution:
    def getIntersectionNode(self, headA, headB):
        dummyA, dummyB = headA, headB # Take dummy nodes

        while dummyA != dummyB:
            dummyA = headB if dummyA is None else dummyA.next 
            dummyB = headA if dummyB is None else dummyB.next
        return dummyA