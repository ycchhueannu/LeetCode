// how to get Leetcode tests to run approximately 10-40% faster, since they do a lot of print outs.
static auto x = [](){
    // turn off sync
    std::ios::sync_with_stdio(false);
    // untie in/out streams
    cin.tie(NULL);
    return 0;
}();

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    int numComponents(ListNode* head, vector<int>& G) {
        
        unordered_set<int> inG(G.begin(), G.end());
        unordered_set<int> s;
        
        int cnt = 0;
        while (head != NULL) {
            if (inG.count(head->val)) { // found
                s.insert(head->val);
            }
            else if (!s.empty()) { // not found, and set is not empty
                unordered_set<int> empty_set;
                s.swap(empty_set); // clear s
                ++cnt;
            }
            head = head->next;
        }
        if (!s.empty())
            ++cnt;
        return cnt;
    }
};