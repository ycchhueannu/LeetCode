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
    /* we assume all values are nonnegative */
    #define INT_MAX 2147483647
    int ans = INT_MAX;
    int prev = -1;
    void binTreeTraverse(TreeNode* root) {
        if (root == NULL)
            return;
        binTreeTraverse(root->left);
        // inorder travese BST assert root->val >= prev, no need to take abs()
        if (prev != -1)
            ans = min(ans, root->val - prev);
        prev = root->val;
        binTreeTraverse(root->right);
        return;
    }
    
    int minDiffInBST(TreeNode* root) {
        binTreeTraverse(root);
        return ans;
    }
};