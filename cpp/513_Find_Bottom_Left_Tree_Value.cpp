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
    struct retAttr {
        int val;
        int level; // note that level is init as -1
        retAttr() : val(0), level(-1) {}
    };
    retAttr *ans = new retAttr;
    
    retAttr* binTreeReverseTraverse(TreeNode* root, int cur_level) {
        retAttr* ret = new retAttr;
        if (root == NULL)
            return ret;
        retAttr* right = binTreeReverseTraverse(root->right, cur_level+1);
        retAttr* left = binTreeReverseTraverse(root->left, cur_level+1);
        
        int max_level = max({left->level, right->level, cur_level, ans->level});

        if (left->level == max_level) { ans->val = left->val;        ans->level = max_level; }
        else if (right->level == max_level) { ans->val = right->val; ans->level = max_level; }
        else if (cur_level == max_level) { ans->val = root->val;     ans->level = max_level; }
        
        return ans;
    }
    int findBottomLeftValue(TreeNode* root) {
        ans = binTreeReverseTraverse(root, 0);
        return ans->val;
    }
};