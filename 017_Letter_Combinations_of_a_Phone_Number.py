from itertools import product as CartesianProduct # Cartesian product
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        d = {'2':['a', 'b', 'c'], '3':['d', 'e', 'f'], '4':['g', 'h', 'i'], '5':['j', 'k', 'l'],
             '6':['m', 'n', 'o'], '7':['p', 'q', 'r', 's'], '8':['t', 'u', 'v'], '9':['w', 'x', 'y', 'z']}
        # assume inputs are valid, can speed up and beat 100% python3 user
        #if all(num not in d for num in digits):
        #    return []
        args = [ d[i] for i in list(digits) ] # list(digits) convert string to list, i.e. "246" -> ['2', '4', '6']
        return (list( map(''.join, CartesianProduct(*args)) ) )

        # 0. pass variable-length arguments in CartesianProduct() (itertools.product)
        # 1. CartesianProduct returns objects stored in tuple format, e.g. ('d', 'g', 'j', 'm'), need to convert to string
        # 2. use map() to convert tuple to string; for only one string, you can use ''.join(tuple)
        # 3. return type is list so we need list() to wrap around map