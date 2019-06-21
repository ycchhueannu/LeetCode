class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        N = len(A)
        i = 0

        # walk up
        while i+1 < N and A[i] < A[i+1]:
            i += 1

        # peak can't be first or last
        if i == 0 or i == N-1:
            return False

        # walk down
        while i+1 < N and A[i] > A[i+1]:
            i += 1

        return i == N-1
        """
        if len(A) < 3:
            return False
        
        up = False
        down = False
        init_up = True
        init_down = True
        for i in range(1, len(A)):
            if A[i] == A[i-1]:
                return False
            elif A[i] > A[i-1]:
                up = True
                if init_up:
                    down = False
                    init_up = False
                if down:
                    return False
            else:
                down = True
                if init_down:
                    up = False
                    init_down = False
                if init_up or up: # init_up: [2, 0, 2]
                    return False
                
        if init_down or init_up: # [0, 1, 2, 3, 4]
            return False
        return True
        """