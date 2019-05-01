class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        S = S.split(' ')
        for idx, word in enumerate(S):
            if word[0] not in vowel:
                word = word[1:] + word[0]
            S[idx] = word + "ma" + "a"*(idx+1)
        return ' '.join(S)