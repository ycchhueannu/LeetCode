class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 0
        
        num_list = []
        freq_list = []
        
        pre = s[0]
        cnt = 1
        for i in range(1, len(s)+1):
            if i == len(s):
                num_list.append(pre)
                freq_list.append(cnt)
            elif s[i] == pre:
                cnt += 1
            else:
                num_list.append(pre)
                freq_list.append(cnt)
                pre = s[i]
                cnt = 1
        ret = 0
        for ni, fi in zip(range(len(num_list)-1), range(len(freq_list)-1)):
            if num_list[ni] != num_list[ni+1]:
                if freq_list[fi] <= freq_list[fi+1]:
                    ret += freq_list[fi]
                else:
                    ret += freq_list[fi+1]
        
        return ret