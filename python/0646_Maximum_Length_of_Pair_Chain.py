class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort(key=lambda x: (x[1], x[0]))
        prev_num = -float("inf")
        cnt = 0
        for pair in pairs:
            if pair[0] > prev_num:
                cnt += 1
                prev_num = pair[1]
        return cnt