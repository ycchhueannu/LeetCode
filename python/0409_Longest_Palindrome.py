class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        odd_sum = 0
        odd_cnt = 0
        even_sum = 0
        for i in d:
            if d[i] % 2:
                odd_sum += d[i]
                odd_cnt += 1
            else:
                even_sum += d[i]
        
        return even_sum + odd_sum - odd_cnt + int(odd_cnt>=1)
        """
        # origin is like this, can be reduced as above!
        if even_sum == 0:
            if odd_cnt == 1:
                return odd_sum
            else:
                return odd_sum - odd_cnt + 1
        if odd_cnt >= 1:
            return even_sum + odd_sum - odd_cnt + 1
        else:
            