class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        # note that "XXXXXLL" and "LXXXLXX" is considered true
        if len(start) != len(end):
            return False
        
        def extract_seq_and_get_next_idx(start, end, i, char_s, char_e):
            d_start_seq = {char_s: 0, char_e: 0}
            d_end_seq = {char_s: 0, char_e: 0}
            while i < len(start):
                if start[i] in [char_s, char_e] and end[i] in [char_s, char_e]:
                    d_start_seq[start[i]] += 1
                    d_end_seq[end[i]] += 1
                    i += 1
                else:
                    break
                    
            if d_start_seq != d_end_seq:
                return -1
            return i
        i = 0
        while i < len(start):
            if start[i] == end[i]:
                i += 1
            else:
                if start[i] == 'X' and end[i] == 'L':
                    i = extract_seq_and_get_next_idx(start, end, i, 'X', 'L')
                    if i == -1:
                        return False
                    elif i == len(start):
                        return True
                elif start[i] == 'R' and end[i] == 'X':
                    i = extract_seq_and_get_next_idx(start, end, i, 'R', 'X')
                    if i == -1:
                        return False
                    elif i == len(start):
                        return True
                else:
                    return False
        return True