class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # trim spaces in LHS and RHS, i.e. " 23.4e5   " -> "23.4e5"
        s = s.lstrip()
        s = s.rstrip()
        # all chars should be in "0~9, e, +, -, and ."
        valid_char = {"0", "1", "2", "3", "4", "5", "6", 
                       "7", "8", "9", "e", "+", "-", "."}
        # space is not allowed
        if any(i not in valid_char for i in s):
            return False
        if all(i in {"+", "-", "."} for i in s):
            return False
        if s.count(".") > 1:
            return False
        
        # deal with numbers with "e" first
        """
        4.e+10 & .3e0 & +.1e1 -> true
        .e1 -> false
        .4 & +5. & -.7 -> true
        """
        if "e" in s:
            if s.count("e") > 1:
                return False
            left, right = s.split("e")
            
            # both left and right should not be empty and no two more "+", "-"
            if not left or not right:
                return False
            if left.count("+") + left.count("-") > 1:
                return False
            if right.count("+") + right.count("-") > 1:
                return False
            
            # right part should be integer with no "."
            if right.count("."):
                return False
            if right.find("+") != -1 and right.index("+") != 0:
                return False
            if right.find("-") != -1 and right.index("-") != 0:
                return False
            if all(i in {"+", "-", "."} for i in right):
                return False
            # left part
            if left.count(".") > 1:
                return False
            if left.find("+") != -1 and left.index("+") != 0:
                return False
            if left.find("-") != -1 and left.index("-") != 0:
                return False
            if all(i in {"+", "-", "."} for i in left):
                return False
        
        else: # "e" not in s
            if s.count("+") + s.count("-") > 1:
                return False
            if s.find("+") != -1 and s.index("+") != 0:
                return False
            if s.find("-") != -1 and s.index("-") != 0:
                return False
        
        return True