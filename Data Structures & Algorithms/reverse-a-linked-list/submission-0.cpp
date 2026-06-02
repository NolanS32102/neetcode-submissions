/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* curr = head;
        vector<int> tempNums;
        while (curr != nullptr) {
            tempNums.push_back(curr->val);
            curr = curr->next;
        }
        
        ListNode *newCurr = head;
        while (tempNums.size() > 0) {
            newCurr->val = tempNums.back();
            tempNums.pop_back();
            newCurr = newCurr->next;
        }
        return head;
    }
};
