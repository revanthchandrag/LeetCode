# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return null
        tempA = headA
        tempB = headB
        pointerASwapped = False
        pointerBSwapped = False
        
        
        
        while tempA != tempB:
            if not pointerASwapped and tempA.next == None:
                tempA = headB
                pointerASwapped = True
            else:
                tempA = tempA.next

            if not pointerBSwapped and tempB.next == None:
                tempB = headA
                pointerBSwapped = True
            else:
                tempB = tempB.next
        return tempA    
            