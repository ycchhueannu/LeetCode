class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        cur_str = "1"
        for i in range(1, n):
            prev = cur_str[0]
            cnt = 1
            next_str = ""
            for cur in cur_str[1:]:
                if cur == prev:
                    cnt += 1
                else:
                    next_str += str(cnt) + prev
                    cnt = 1
                    prev = cur
            next_str += str(cnt) + prev
            cur_str = next_str
        
        return cur_str