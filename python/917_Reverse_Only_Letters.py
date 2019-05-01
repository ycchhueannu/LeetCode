class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        S = list(S)
        low = 0
        high = len(S)-1
        while low < high:
            if not S[high].isalpha():
                high -= 1
                continue
            if not S[low].isalpha():
                low += 1
                continue
            S[low], S[high] = S[high], S[low]
            low += 1
            high -= 1
        return ''.join(S)