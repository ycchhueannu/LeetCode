class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        s3 = "0110"
        if N <= 3:
            return s3[K-1]
        cur = K
        flip = False
        half = 2 << (N-2) # (N-1) - 1
        while cur > 4: # base case len = 4
            if cur > half:
                flip = not flip
                cur -= half
            half >>= 1
            #print(cur, half)
        
        if flip:
            s3 = "1001"
        return s3[cur-1]
        
        
        """
        s = "0"
        flip = lambda x: '1' if x == '0' else '0'   
        for i in range(1, N): # current i is row i+1 
            if i % 2:
                s += ''.join(map(flip,s))    
            else:
                s += s[::-1]
            #print(s)
        return s[K-1]
        """