class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # perfect square will always end in 0, 1, 4, 5, 6, 9
        if num % 10 not in [0, 1, 4, 5, 6, 9]:
            return False
        low = 0
        high = num
        while low <= high:
            mid = (low + high) // 2
            mid2 = mid**2
            if mid2 > num:
                high = mid - 1
            elif mid2 < num:
                low = mid + 1
            else:
                return True
        return False