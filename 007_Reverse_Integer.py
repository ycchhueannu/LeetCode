class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        # assume (Min. =) -2147483648 < x < 2147483647 (= Max.)
        # some 'facts': if y is not in range, i.e. y > Max. or y < Min.
        # then Max. & y != y if y >= 0, and Min. & y != Min. if y < 0
        
        if x > 0:
            x = x % (1<<31)
        else:
            x = x % (-1<<31)
            
        s = str(x)
        Max, Min = (1<<31) - 1, -1<<31
        
        if s[0] == '-':
            num = int('-'+s[:0:-1])
        else:
            num = int(s[::-1])
            
        #print(num)
        if (num >= 0) and (num & Max == num):
            return num
        elif (num < 0) and (num & Min == Min):
            return num
        else:
            return 0