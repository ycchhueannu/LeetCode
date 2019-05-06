class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if set(B) - set(A): # A doesn't have all chars in B
            return -1
        elif B in A:
            return 1
        # should be at least 2 string of A
        start = 0
        cnt = 2
        while start < len(A):
            if B[0] not in A[start:]:
                break
            i = A[start:].index(B[0]) # find the first matched char
            i += start
            tmpA = A[i:] + A
            # while loop is the case when B is much longer than A
            while len(tmpA) < len(B):
                cnt += 1
                tmpA += A
            # if B is initially smaller than A, will not enter 
            # while loop. Also, the following if also checks the 
            # last time tmpA concatenate A but exceed B's length
            if B in tmpA:
                return cnt
            else:
                cnt = 2
                start = i+1
        return -1