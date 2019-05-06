class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        ret = []
        ist = sorted(zip(indexes, sources, targets), key=lambda x: x[0])
        indexes, sources, targets = zip(*ist)
        pre_end = 0
        for i in range(0, len(indexes)):
            if sources[i] == S[indexes[i]:indexes[i]+len(sources[i])]:
                ret.append(S[pre_end:indexes[i]])
                ret.append(targets[i])
                pre_end = indexes[i] + len(sources[i])
        if pre_end < len(S):
            ret.append(S[pre_end:])
        return ''.join(ret)