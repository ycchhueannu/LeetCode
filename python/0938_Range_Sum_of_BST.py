# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        s = 0
        if not root:
            return 0
        elif root.val >= L and root.val <= R:
            s += root.val + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)
        elif root.val < L:
            s += self.rangeSumBST(root.right, L, R)
        elif root.val > R:
            s += self.rangeSumBST(root.left, L, R)
        return s