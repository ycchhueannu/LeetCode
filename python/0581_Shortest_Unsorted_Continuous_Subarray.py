class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sort_nums = sorted(nums)
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] != sort_nums[left]:
                while nums[right] == sort_nums[right]:
                    right -= 1
                return right - left + 1
            left += 1
        return 0