class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)
        target_mod2 = target % 2
        i = int((2*target+0.25)**0.5 - 0.5) # i >= -0.5 + sqrt(...)
        max_pos = i*(i+1)/2 # current max position
        while True:
            if max_pos >= target and max_pos % 2 == target_mod2:
                return i
            i += 1
            max_pos += i
        return -1
        """
        target = abs(target)
        i = 1
        max_pos = 0 # current max position
        target_mod2 = target % 2
        while True:
            max_pos += i
            if max_pos % 2 == target_mod2 and target <= max_pos:
                return i
            i += 1
        return -1
        """
"""
# just enumerate all positions you will know numbers are
# 'symmetric', i.e. negative doesn't matter
set would be odd odd even even odd odd even even ...
1   num # 1
2   num # 1 3
4   num # 0 2 4 6
6   num # 0 2 4 6 8 10
8   num # 1 3 5 7 9 11 13 15
11  num # 1 3 5 7 9 11 13 15 17 19 21
15  num # 0 2 4 6 8 10 12 14 16 18 29 22 24 26 28
19  num # 0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36
23  num # 1 ~ 45 (odd)
28  num # 1 ~ 55 (odd)
34  num # 0 ~ 66 (even)
        # ...
we only need to track the maximum odd/even number
rules are as follows:
each step i, we already know maximum number is odd or even
if I take i step, then the maximum position I can reach is
i*(i+1)/2 -> we want target <= i*(i+1)/2, directly solve i
"""