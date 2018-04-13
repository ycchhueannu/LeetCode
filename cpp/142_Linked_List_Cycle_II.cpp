/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

// how to get Leetcode tests to run approximately 10-40% faster, since they do a lot of print outs.
static auto x = [](){
    // turn off sync
    std::ios::sync_with_stdio(false);
    // untie in/out streams
    cin.tie(NULL);
    return 0;
}();

class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        if (head == NULL)
            return NULL;
        ListNode *hop1 = head;
        ListNode *hop2 = head;

        hop1 = hop1->next;
        hop2 = hop2->next;
        if (hop2 != NULL)
            hop2 = hop2->next;
        while (hop2 != NULL) {
            if (hop1 == hop2) { // cycle dectect
                hop1 = head;
                while (hop1 != hop2) { // find cycle start position
                    hop1 = hop1->next;
                    hop2 = hop2->next;
                }
                return hop1;
            }
            hop1 = hop1->next;
            hop2 = hop2->next;
            if (hop2 != NULL)
                hop2 = hop2->next;

        } // end while
        
        return NULL;
    }
};

/*
let two pointers meet after k steps,
2k = LEN_NO_CYCLE + #cycle * LEN_CYCLE + m (0 <= m < LEN_CYCLE)
k  = LEN_NO_CYCLE                      + m
Thus, k = n * |c| (#cycle * LEN_CYCLE)
to find LEN_NO_CYCLE, e.g. LEN_NO_CYCLE = k - m = n * |c| - m
let n = 1, then "|c| - m" is the number of steps to complete
traversing the cycle, and is equal to LEN_NO_CYCLE
*/