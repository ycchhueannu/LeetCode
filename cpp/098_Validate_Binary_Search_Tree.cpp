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
    // edge cases: [2147483647, 2147483647], [2147483647], [-2147483648,null,2147483647]
    const long long int MY_INT_MIN = -2147483649; // -1 << 31 - 1
    const long long int MY_INT_MAX = 2147483648; // 1 << 31
    bool isValidBST(TreeNode* root) {
        return intervalBST(root, MY_INT_MIN, MY_INT_MAX);
    }
    bool intervalBST(TreeNode* root, const long long int lb,  const long long int ub) {
        //if (root != NULL)
        //    printf("root val: %d, lb: %lld, ub: %lld\n", root->val, lb, ub);
        if (root == NULL)
            return true;
        else if (root->val >= ub || root->val <= lb)
            return false;
        else if (root->left == NULL && root->right == NULL) // speed up?
            return true;
        else {
            return intervalBST(root->left, lb, min((long long int)root->val, ub)) && \
                   intervalBST(root->right, max((long long int)root->val, lb), ub);
        }
    }
};