class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # ' '.join([i[::-1] for i in s.split(' ')]) is slower
        return ' '.join(list(map(lambda x: x[::-1], s.split(' '))))