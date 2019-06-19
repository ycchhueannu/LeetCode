class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        ret = []
        
        pre = S[0]
        cnt = 1
        cur_start = 0
        for i in range(1, len(S)):
            if S[i] == pre:
                cnt += 1
            else:
                if cnt >= 3:
                    ret.append([cur_start, i-1])
                
                pre = S[i]
                cnt = 1
                cur_start = i
        # i will be len(S)-1 when exiting the for loop, no need to minus 1
        if cnt >= 3:
            ret.append([cur_start, i])
        
        return ret