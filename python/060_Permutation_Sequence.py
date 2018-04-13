from math import factorial # usage: factorial(n), e.g. factorial(5) = 5! = 120
class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def findFirstNumber(l, num):
            p = factorial(len(l)-1)
            q, r = num // p, num % p
            first_chr = str(l[q])
            l.remove(l[q])
            if r == 0:
                return first_chr + ''.join(map(str, sorted(l)))
            elif r == p - 1:
                return first_chr + ''.join(map(str, sorted(l, reverse=True)))
            else:
                return first_chr + findFirstNumber(l, r)
        
        return findFirstNumber(list(range(1, n+1)), k-1)