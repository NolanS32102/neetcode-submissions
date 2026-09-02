"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        
        oldHead = head
        nodeMap = {None: None}
        
        while head is not None:
            nodeMap[head] = Node(head.val)
            head = head.next

        newHead = nodeMap[oldHead]
        while oldHead is not None:
            nodeMap[oldHead].next = nodeMap[oldHead.next]
            nodeMap[oldHead].random = nodeMap[oldHead.random]
            oldHead = oldHead.next

        return newHead
