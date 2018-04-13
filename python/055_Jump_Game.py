class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True
        
        max_edge = 0
        for cur in range(0, len(nums)):
            if (cur == max_edge) and (not nums[cur]):
                return False
            elif cur + nums[cur] > max_edge:
                max_edge = cur + nums[cur]
                if max_edge >= len(nums) - 1:
                    return True