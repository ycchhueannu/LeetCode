class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(t) > len(s):
            return ""
        
        
        cnt_dict = {}
        for t_chr in t:
            if t_chr not in cnt_dict:
                cnt_dict[t_chr] = 1
            else:
                cnt_dict[t_chr] += 1

        dist = []
        dist_st = 0 # start index in list dist
        min_start, min_end = 0, len(s) # init minimum end as length of s, which means not found
        num_miss = len(cnt_dict.keys()) # number of missing character
        for idx, s_chr in enumerate(list(s)): # list(s) convert "abc" into ['a', 'b', 'c']
            if (s_chr in cnt_dict):
                cnt_dict[s_chr] -= 1
                dist.append(idx)
                if cnt_dict[s_chr] == 0:
                    num_miss -= 1
                
                if num_miss == 0: # can speed up
                    if min_end - min_start > dist[-1] - dist[0]:
                        min_end = dist[-1]
                        min_start = dist[0]
                        
                    char = s[dist[dist_st]]
                    while cnt_dict[char] < 0:
                        cnt_dict[char] += 1;
                        dist_st += 1
                        if min_end - min_start > dist[-1] - dist[dist_st]:
                            min_end = dist[-1]
                            min_start = dist[dist_st]
                            
                        char = s[dist[dist_st]]
                        
                        
        if min_end == len(s): # not found
            return ""
        return s[min_start:min_end+1]