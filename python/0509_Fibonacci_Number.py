class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        fn_1, fn = 0, 1
        if N == 0:
            return 0
        elif N == 1:
            return 1
        for i in range(2, N+1):
            fn, fn_1 = fn+fn_1, fn
        return fn