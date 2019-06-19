class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zi = 0
        for i in range(0, len(nums)):
            if nums[i]:
                if i != zi:
                    nums[i], nums[zi] = nums[zi], nums[i]
                zi += 1
        """
        from collections import deque
        q = deque()
        for i in range(0, len(nums)):
            if nums[i] == 0:
                q.append(i)
            elif len(q):
                zi = q.popleft()
                nums[zi], nums[i] = nums[i], 0
                q.append(i)
        return nums
        """