class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort(reverse=True)
        for i in range(0, len(A)-2):
            if A[i+1] + A[i+2] > A[i]:
                return A[i] + A[i+1] + A[i+2]
        return 0