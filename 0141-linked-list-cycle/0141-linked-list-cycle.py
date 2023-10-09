# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast is not None:
            slow = slow.next
            if fast.next is not None:
                fast = fast.next.next
            else:
                return False
            
            if slow == fast:
                return True
        return False    
        