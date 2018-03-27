class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if "0" in [num1, num2]:
            return "0"
        elif "1" in [num1, num2]:
            res = num2 if num1 == "1" else num1
            return res
        
        
        len1, len2 = len(num1), len(num2)
        res = [0] * (len1 + len2) # initialize, A LOT faster than [0 for _ in range(len1+len2)]
        
        l_int = int # local int(), for speed up
        
        #strMulstr = lambda x: l_int(v1) * l_int(x)
        #addSum = lambda x, y: x + y
        
        for i, v1 in enumerate(num1):
            digitToAdd = map(lambda x: l_int(v1)*l_int(x), num2) # map is also iterable, no need to convert to list
            res[i:i+len2] = map(lambda x, y: x+y, res[i:i+len2], digitToAdd) # convert map to list is redundant here !! (strange?)
        
        #print(res)
        res = res[::-1] # reverse
        res = res[res.index(0)+1:]
        #print(res)
        
        carry = 0
        
        for i, val in enumerate(res):
            val += carry
            carry, res[i] = val // 10, val % 10
        
        if carry != 0: # carry may not be 0
            res.append(carry)
        #print("final", res)
        l_str = str # local str(), for speed up
        return (''.join([l_str(c) for c in res]))[::-1]