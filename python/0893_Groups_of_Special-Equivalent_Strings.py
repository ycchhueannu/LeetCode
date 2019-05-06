class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        return len(set("".join(sorted(s[::2])) + "".join(sorted(s[1::2])) for s in A))