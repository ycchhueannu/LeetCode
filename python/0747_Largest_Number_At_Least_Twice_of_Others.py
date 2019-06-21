class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first_max = -1
        second_max = -1
        idx = -1
        for i in range(0, len(nums)):
            if nums[i] > first_max:
                first_max, second_max = nums[i], first_max
                idx = i
            elif nums[i] > second_max:
                second_max = nums[i]
        
        if second_max*2 > first_max:
            return -1
        return idx