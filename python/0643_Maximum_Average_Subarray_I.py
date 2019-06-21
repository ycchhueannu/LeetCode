class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        cur_sum = sum(nums[:k])
        max_sum = cur_sum
        for i in range(k, len(nums)):
            cur_sum += nums[i] - nums[i-k]
            if cur_sum > max_sum:
                max_sum = cur_sum

        return max_sum / float(k)