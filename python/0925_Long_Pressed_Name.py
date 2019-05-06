class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        if len(name) >= len(typed):
            if name == typed:
                return True
            return False
        
        i = 0
        j = 0
        match = False
        while i < len(name) and j < len(typed):
            if name[i] == typed[j]:
                match = True
                i += 1
                j += 1
            elif name[i] != typed[j]:
                if match and typed[j] == name[i-1]:
                    j += 1
                else:
                    return False

        if i == len(name) and all(name[-1] == _ for _ in list(typed[j:])):
            return True
        else:
            return False