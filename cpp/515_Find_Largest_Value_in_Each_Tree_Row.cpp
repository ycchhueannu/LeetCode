// how to get Leetcode tests to run approximately 10-40% faster, since they do a lot of print outs.
static auto x = [](){
    // turn off sync
    std::ios::sync_with_stdio(false);
    // untie in/out streams
    cin.tie(NULL);
    return 0;
}();

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> largestValues(TreeNode* root) {
        #define NEG_INF -2147483648
        vector<int> ans;
        queue<TreeNode*> q;
        queue<TreeNode*> q_next; // next level of TreeNode
        q.push(root);
        int maxNum = NEG_INF;
        while (!q.empty()) {
            TreeNode* cur = q.front();
            q.pop();
            if (cur == NULL)
                continue;
            if (cur->left != NULL)
                q_next.push(cur->left);
            if (cur->right != NULL)
                q_next.push(cur->right);
            //printf("size q = %d, q_next = %d, current val:%d, maxNum:%d\n", q.size(), q_next.size(), cur->val, maxNum);
            maxNum = max(maxNum, cur->val);
            //printf("maxNum = %d\n", maxNum);
            if (q.empty()) {
                ans.push_back(maxNum);
                maxNum = NEG_INF; // if float, use -std::numeric_limits<float>::infinity()
                swap(q, q_next);
            }
        } // end while
        //printf("size q = %d, q_next = %d\n", q.size(), q_next.size());
        return ans;
    }
};