class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if r*c != len(nums)*len(nums[0]) or (r == len(nums) and c == len(nums[0])):
            return nums
        
        ret = []
        new_r = []
        for row in nums:
            for e in row:
                if len(new_r) == c:
                    ret.append(new_r)
                    new_r = [e]
                else:
                    new_r.append(e)
        ret.append(new_r)
        return ret