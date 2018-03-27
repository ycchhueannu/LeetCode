class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stk = []
        pair = { ')': '(', ']': '[', '}': '{' }
        for char in list(s):
            if char in ['(', '[', '{']:
                stk.append(char)
            else: # char in [')', ']', '}']:
                if len(stk) == 0:
                    return False
                if stk[-1] == pair[char]:
                    del stk[-1]
                else:
                    return False
        if len(stk) == 0:
            return True
        else:
            return False