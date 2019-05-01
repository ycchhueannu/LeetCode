class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(chars) == 1: # compress only when repeat
            return 1
        cnt = 1
        i = 1
        while i < len(chars):
            update_i = True
            if len(chars[i-1]) > 1: # e.g. "a3"
                if chars[i-1][0] == chars[i]:
                    chars[i-1] = chars[i-1][0] + str(int(chars[i-1][1:])+1)
                    del chars[i]
                    update_i = False
            else:
                if chars[i-1] == chars[i]:
                    chars[i-1] += "2"
                    del chars[i]
                    update_i = False
            if update_i:
                i += 1
                
        # O(1) extra space
        for idx, val in enumerate(chars):
            cur = idx
            for _ in val:
                if cur == idx:
                    chars[cur] = _
                else:
                    chars.insert(cur, _)
                cur += 1
                
        return len("".join(chars))