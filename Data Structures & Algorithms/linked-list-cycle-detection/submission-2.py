# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while (slow is not None) and (fast is not None):
            slow = slow.next
            if fast.next is not None:
                fast = fast.next.next
            else:
                fast = fast.next
            if (slow is not None) and (fast is not None) and slow == fast:
                return True
        
        return False
