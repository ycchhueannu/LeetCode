# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        import itertools
        if not N % 2: # even nodes can't make FBT
            return []
        ret = []
        cur_node = TreeNode(0)
        if N == 1:
            return [cur_node]
        for i in range(1, N, 2):
            left = self.allPossibleFBT(i)
            right = self.allPossibleFBT(N-1-i)
            #for l, r in itertools.product(left, right):
            for l in left:
                for r in right:
                    cur_node = TreeNode(0)
                    cur_node.left = l
                    cur_node.right = r
                    ret.append(cur_node)
        return ret