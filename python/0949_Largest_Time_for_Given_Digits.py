class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        max_num = 2359
        if A.count(6) + A.count(7) + A.count(8) + A.count(9) > 2:
            return ""
        elif A.count(3) == 4 or A.count(4) == 4 or A.count(5) == 4:
            return ""
        else:
            from itertools import permutations
            permA = permutations(A)
            cur_max = -1
            ret = ""
            for cur_perm in permA:
                a, b, c, d = cur_perm
                cur_num = a*1000 + b*100 + c*10 + d
                if (cur_num > cur_max) and (a*10+b < 24) and (c*10+d <= 59):
                    ret = str(a)+str(b)+":"+str(c)+str(d)
                    cur_max = cur_num
            return ret