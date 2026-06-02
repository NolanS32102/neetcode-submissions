/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} head
     * @return {boolean}
     */
    hasCycle(head) {
        let curr = head;
        const visitedNodes = new Set();
        while (curr !== null) {
            if (visitedNodes.has(curr)) {
                return true;
            }
            visitedNodes.add(curr);
            curr = curr.next;
        }
        return false;
    }
}
