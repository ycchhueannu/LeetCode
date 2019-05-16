class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        i = num % 9 # observation
        if i:
            return i
        else:
            return 9
        """
        digit = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
        transform = {'1': [9, 1, 2, 3, 4, 5, 6, 7, 8],
                '2': [9, 2, 4, 6, 8, 1, 3, 5, 7],
                '4': [9, 4, 8, 3, 7, 2, 6, 1, 5],
                '7': [9, 7, 5, 3, 1, 8, 6, 4, 2],
                '8': [9, 8, 7, 6, 5, 4, 3, 2, 1],
                '5': [[9, 1, 2, 3, 4, 5, 6, 7, 8], 
                      [4, 5, 6, 7, 8, 9, 1, 2, 3]],
                '3': [9, 3, 6],
                '6': [9, 6, 3],
                '9': [9],
                '0': [0]}
        d = {i: 0 for i in digit}
        for i in str(num):
            d[i] += 1
            
        ret = 0
        for i in d:
            if d[i] == 0:
                continue
            #print("========")
            #print("now", i, d[i])
            if i in {'1', '2', '4', '7', '8'}:
                d[i] %= 9
                #print(d[i], transform[i][d[i]])
                ret += transform[i][d[i]]
            elif i in {'3', '6'}:
                d[i] %= 3
                #print(d[i], transform[i][d[i]])
                ret += transform[i][d[i]]
            elif i == '9':
                d[i] %= 1
                #print(d[i], transform[i][d[i]])
                ret += transform[i][d[i]]
            elif i == '5':
                if d[i] % 2: # odd
                    d[i] = (d[i] - 1)//2 + 1
                    d[i] %= 9
                    #print(d[i], transform[i][1][d[i]])
                    ret += transform[i][1][d[i]]
                else:
                    d[i] = d[i] // 2
                    d[i] %= 9
                    #print(d[i], transform[i][0][d[i]])
                    ret += transform[i][0][d[i]]
        # even if all digits have largest number, 9, it
        # won't exceed 81, which is less than 100
        if ret >= 10: 
            ret = ret//10 + ret%10
            if ret >= 10:
                ret = ret//10 + ret%10
        return ret
        """
        
        # n's 1 to 9 will end in...
        # 9 -> [9], 9, 9, 9, 9, ...
        # 8 -> [8, 7, 6, 5, 4, 3, 2, 1, 9], 8 ...
        # 7 -> [7, 5, 3, 1, 8, 6, 4, 2, 9], 7, ...
        # 6 -> [6, 3, 9], 6, 3, 9, ...
        # 5 -> 5, 1, 6, 2, 7, ... [minus 4, plus 5]
        #      odd: [5, 6, 7, 8, 9, 1, 2, 3, 4], 5 ...
        #      even:[1, 2, 3, 4, 5, 6, 7, 8, 9], 1 ...
        # 4 -> [4, 8, 3, 7, 2, 6, 1, 5, 9], 4, 8 ...
        # 3 -> [3, 6, 9], 3, 6, 9, ...
        # 2 -> [2, 4, 6, 8, 1, 3, 5, 7, 9], 2, 4, ...
        # 1 -> [1, 2, 3, 4, 5, 6, 7, 8, 9], 1, 2, ...