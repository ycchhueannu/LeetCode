class Solution(object):
    def sortArrayByParity(self, A):
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
        evenA.extend(oddA)
        return evenA