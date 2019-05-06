class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        origin_num = num # original number
        
        element_num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        element_sym = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", 
                      "D", "CM", "M"]
        assert len(element_num) == len(element_sym)
        # list of symbol and value
        sv_list = [(sym, num) for sym, num in zip(element_sym, element_num)]
        vs_list = [(num, sym) for sym, num in zip(element_sym, element_num)]
        # build two-way dictionary
        sym2val = dict(sv_list)
        val2sym = dict(vs_list)

        element_cnt = {i: 0 for i in element_num}
        # stack is the copy of element_num
        stack = [i for i in element_num]
        
        num = origin_num # assign origin_num back to num
        while num > 0:
            top = stack[-1]
            if num >= top:
                num -= top
                element_cnt[top] += 1
            else:
                stack.pop()
        
        ret = ""
        for num, sym in zip(element_num[::-1], element_sym[::-1]):
            ret += sym * element_cnt[num]
        
        return ret