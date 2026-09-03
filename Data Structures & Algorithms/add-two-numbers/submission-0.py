# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        addedList = ListNode()
        curr = addedList

        carry = 0
        while (l1 is not None) or (l2 is not None):
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0

            sumOfNodes = val1 + val2 + carry
            carry = sumOfNodes // 10

            curr.next = ListNode(sumOfNodes % 10)
            curr = curr.next
            sumOfNodes = 0

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        if carry != 0:
            curr.next = ListNode(carry)

        return addedList.next

    