class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        cnt = 0
        for num in range(1, N+1):
            sn = str(num)
            if '3' in sn or '7' in sn or '4' in sn:
                continue
            if '2' in sn or '5' in sn or '6' in sn or '9' in sn:
                cnt += 1
        return cnt
        
        """
        # base case:
        bc_ans = {1: 0, 2: 1, 3: 1, 4: 1, 5: 2, 6: 3, 7: 3, 8: 3, 9: 4}
        if N < 10:
            return bc_ans[N]
        # we only care about numbers only contain 0, 1, 2, 5, 6, 8, 9
        # if a number has 3, 4, 7, then it's not valid. Note that
        # a number is valid iff it has 2, 5, 6, or 9 (at least one)
        cnt = 0
        valid = set({2, 5, 6, 9})
        for i in range(10, N+1):
            si = str(i)
            if set(si).isdisjoint({'3', '4', '7'}):
                # remove most significant (digit) number ("169" -> "69")
                # if use 'si[i:] in valid', numbers like 806 will fail 
                if int(si[0]) in valid or int(si[1:]) in valid:
                    cnt += 1
                    valid.add(int(si))
        return len(valid)
        """