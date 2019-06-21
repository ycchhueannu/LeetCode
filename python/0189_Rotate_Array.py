class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        if k == 0:
            return
        num_change = 0
        start_index = 0
        # note that if I don't count the number of change and let
        # start index be 0, then it will fail if the case is 
        # [1, 2, 3, 4, 5, 6], k = 2
        while num_change < len(nums):
            cur = start_index
            prev = nums[start_index]
            while True:
                nex = (cur + k) % len(nums)
                nums[nex], prev = prev, nums[nex]
                cur = nex
                num_change += 1
                if nex == start_index:
                    break
            start_index += 1
            #print(nums)
        return
        """
        i = 0
        tmp = nums[-k:] + nums[:-k]
        for i in range(0, len(nums)):
            nums[i] = tmp[i]
        return nums
        """