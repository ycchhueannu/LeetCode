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
    TreeNode* pruneTree(TreeNode* root) {
        if (root == NULL)
            return NULL;
        root->left = pruneTree(root->left); // left subtree
        root->right = pruneTree(root->right); // right subtree
        // (root->left == NULL) && (root->right == NULL) && (root->val == 0)
        if ( !(root->left || root->right || root->val) )
            return NULL;

        return root;
    }
};