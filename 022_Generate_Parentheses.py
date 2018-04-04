class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        traverse = {}
        ans = []
        def gen(string, l, r):
            if string in traverse:
                return
            traverse[string] = 1
            #print("string:", string, ", l and r =", l, r)
            
            if (l + r == 0): # l == 0 and r == 0
                if(len(string) == 2*n):
                    ans.append(string)
                return
            
            tmpl, tmpr = l, r
            suffix = ""
            while r > l:
                r -= 1
                suffix += ')'
                gen(string + suffix, l, r)
                
            l, r = tmpl, tmpr
            suffix = ""
            while l > 0:
                l -= 1
                suffix += '('
                gen(string + suffix, l, r)
                
            return
        
        gen("", n, n) # remaining number of left and right parentheses
        
        return list(set(ans))