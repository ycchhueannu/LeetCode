class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        num1 = [str(int(d)) for d in version1.split('.')]
        num2 = [str(int(d)) for d in version2.split('.')]
        
        len_min = min(len(num1), len(num2))
        for n1, n2 in zip(num1[:len_min], num2[:len_min]):
            if int(n1) > int(n2):
                return 1
            elif int(n1) < int(n2):
                return -1
        if num1[len_min:]:
            if int(''.join(num1[len_min:])) == 0:
                return 0
            else:
                return 1
        if num2[len_min:]:
            if int(''.join(num2[len_min:])) == 0:
                return 0
            else:
                return -1
        
        return 0 # case when "01" and "1"