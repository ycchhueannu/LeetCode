# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def get_preorder_string(self, t):
        if not t:
            return ""
        if not t.left and not t.right:
            return str(t.val)
        elif not t.right:
            return str(t.val) + '(' + self.get_preorder_string(t.left) + ')'
        else:
            return str(t.val) + '(' + self.get_preorder_string(t.left) + ')' + \
            '(' + self.get_preorder_string(t.right) + ')'
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        return self.get_preorder_string(t)