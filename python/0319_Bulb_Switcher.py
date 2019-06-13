class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(n**0.5)
        """
        # will get TLE
        cnt = [1] * n
        for i in range(2, n+1):
            for j in range(1, n//i + 1):
                k = i*j
                if k > n:
                    break
                else:
                    cnt[k-1] += 1
        ans = 0
        for i in cnt:
            if i % 2:
                ans += 1
        return ans
        """