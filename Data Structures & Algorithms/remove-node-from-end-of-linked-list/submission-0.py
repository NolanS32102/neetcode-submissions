# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr is not None:
            length += 1
            curr = curr.next
        
        index = length - n
        if index == 0:
            return head.next
            
        prev = head
        for i in range(index - 1):
            prev = prev.next
        
        if prev.next is not None:
            prev.next = prev.next.next
        return head
        