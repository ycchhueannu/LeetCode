class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sum_A = sum(A)
        sum_B = sum(B)
        set_A = set(A)
        set_B = set(B)
        for a in set_A:
            # sum_A - a + b == sum_B - b + a
            b = a + (sum_B-sum_A)//2
            if b in set_B:
                return [a, b]