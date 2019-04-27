class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        symTable = {"I": 1, "V": 5, "X": 10, "L":50, 
                        "C": 100, "D": 500, "M": 1000, 
                        "IV": 4, "IX": 9, "XL": 40, "XC": 90, 
                        "CD": 400, "CM":900}
        num = 0
        i = 0
        while i < len(s):
            if i < len(s)-1:
                if s[i]+s[i+1] in symTable:
                    num += symTable[s[i]+s[i+1]]
                    i += 2
                else:
                    num += symTable[s[i]]
                    i += 1
            else:
                num += symTable[s[i]]
                i += 1
        
        return num