class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if path == '':
            return ''
        
        seq = filter(lambda x: x not in ('', '.'), path.split('/')) # remove '' and '.'
        #print(seq)
        stk = []
        for val in seq:
            if (val == '..'):
                if stk != []: del stk[-1]
                continue
            stk.append(val)
        #print(stk)
        return '/' + '/'.join(stk)