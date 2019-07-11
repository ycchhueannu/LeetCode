class Solution(object):
    def minHeightShelves(self, books, shelf_width):
        """
        :type books: List[List[int]]
        :type shelf_width: int
        :rtype: int
        """
        if len(books) == 0:
            return 0
        n = len(books)
        dp = [0] * n
        dp[0] = books[0][1]
        dp.append(0) # trick used in line 24 (if j == 0)
        for i in range(1, n):
            dp[i] = dp[i-1] + books[i][1] # i-th books is on the new shelf
            cur_w = books[i][0]
            cur_h = books[i][1]
            for j in range(i-1, -1, -1): # add books until exceed shelf width
                cur_w += books[j][0]
                if cur_w > shelf_width:
                    break
                else:
                    if books[j][1] > cur_h:
                        cur_h = books[j][1]
                    dp[i] = min(dp[i], cur_h + dp[j-1])
        
        return dp[n-1]
        """
        # version 1 will get TLE, O(n^3) method, BUT can solve
        # any continuous sequences of books (no need to start from 0)
        # DP formula (correct but slow): let H[i..j] be the optimal
        # solution from book[i] to book[j], then, 
        #           { book[i][1],                     if i == j
        # H[i..j] = { 0,                              if j < i
        #           { min  {H[i..k] + H[k+1..j]},     if j > i
        #            i<=k<j
        # Also, we need to know that books can't exceed shelf's width;
        # that is, if sum(books[i..j][width]) <= shelf width, then H[i..j]
        # is equal to the maximum book's width in book[i..j]. Otherwise,
        # we should split into two parts.
        if len(books) == 0:
            return 0
        n = len(books)
        
        # width/height sum from i to j
        w_sum = [books[0][0]]
        h_sum = [books[0][1]]
        for i in range(1, n):
            w_sum.append(w_sum[-1] + books[i][0])
            h_sum.append(h_sum[-1] + books[i][1])
        w_sum.append(0) # let w_sum[-1] = 0
        h_sum.append(0) # let h_sum[-1] = 0
        
        dp = [[0]*n for _ in range(n)]
        h_max = [[0]*n for _ in range(n)] # book's max height from i to j
        for i in range(0, n):
            dp[i][i] = books[i][1]
            h_max[i][i] = books[i][1]
        
        for i in range(0, n):
            cur = books[i][1]
            for j in range(i+1, n):
                if books[j][1] > cur:
                    cur = books[j][1]
                h_max[i][j] = cur
        
        for l in range(2, n+1):
            for i in range(0, n-l+1):
                j = i + l - 1
                if w_sum[j] - w_sum[i-1] <= shelf_width:
                    cur = h_max[i][j]
                else:
                    cur = h_sum[j] - h_sum[i-1]
                    for k in range(i, j):
                        if dp[i][k] + dp[k+1][j] < cur:
                            cur = dp[i][k] + dp[k+1][j]
                dp[i][j] = cur
        
        return dp[0][n-1]
        """