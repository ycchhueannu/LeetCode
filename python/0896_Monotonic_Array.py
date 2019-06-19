class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) == 1:
            return True
        is_increase, is_decrease = None, None
        for i in range(1, len(A)):
            if A[i] < A[i-1]:
                is_decrease = True
                if is_increase:
                    return False
            elif A[i] > A[i-1]:
                is_increase = True
                if is_decrease:
                    return False
        return True