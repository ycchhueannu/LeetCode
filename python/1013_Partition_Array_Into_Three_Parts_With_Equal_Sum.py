class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        sum_A = sum(A)
        if sum_A % 3:
            return False
        part_sum = sum_A // 3
        ps = 0
        cnt = 0
        for a in A:
            ps += a
            if ps == part_sum:
                ps = 0
                cnt += 1
        return (not ps) and (cnt == 3)