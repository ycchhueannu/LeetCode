class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        oddA = []
        evenA = []
        for a in A:
            if a % 2:
                oddA.append(a)
            else:
                evenA.append(a)
        A[::2] = evenA
        A[1::2] = oddA
        return A