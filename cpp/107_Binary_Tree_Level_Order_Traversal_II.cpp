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
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        vector<vector<int>> ans;
        queue<TreeNode*> q;
        queue<int> q_level; // level in current node
        q.push(root);
        q_level.push(0);
        while (!q.empty()) {
            TreeNode* cur = q.front(); q.pop();
            int cur_l = q_level.front(); q_level.pop();
            if (cur == NULL)
                continue;
            q.push(cur->left);
            q_level.push(cur_l+1);
            q.push(cur->right);
            q_level.push(cur_l+1);
            
            if (ans.size() <= cur_l) {
                vector<int> vec = {cur->val};
                ans.push_back(vec);
            }
            else { // ans.size() == cur_l + 1 
                ans[cur_l].push_back(cur->val);
            }
        }        
        
        
        #include <algorithm>
        std::reverse(ans.begin(), ans.end());
        return ans;
    }
};