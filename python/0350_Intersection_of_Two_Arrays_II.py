class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d1 = {}
        ret = []
        for i in nums1:
            if i not in d1:
                d1[i] = 1
            else:
                d1[i] += 1
        for i in nums2:
            if i in d1 and d1[i]:
                d1[i] -= 1
                ret.append(i)
        return ret