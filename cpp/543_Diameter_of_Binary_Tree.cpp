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
    struct ReturnAttr {
        int max_d; // maximum depth, either by left subtree or by right subtree
        int diameter; // maximum diameter
        ReturnAttr() : diameter(0), max_d(0) {}
    };
    
    ReturnAttr* BinTreeTraverse(TreeNode* root) {
        ReturnAttr *ret = new ReturnAttr;
        if (root == NULL)
            return ret;
        
        ReturnAttr* leftAttr = BinTreeTraverse(root->left);
        ReturnAttr* rightAttr = BinTreeTraverse(root->right);
            
        int cross_diameter = leftAttr->max_d + rightAttr->max_d;
        ret->max_d = 1 + max(leftAttr->max_d, rightAttr->max_d);
        // original max can't do more than two entries..sucks
        ret->diameter = std::max({leftAttr->diameter, rightAttr->diameter, cross_diameter});
        return ret;
    }
    
    int diameterOfBinaryTree(TreeNode* root) {
        ReturnAttr* ans = BinTreeTraverse(root);
        return ans->diameter;
    }
};