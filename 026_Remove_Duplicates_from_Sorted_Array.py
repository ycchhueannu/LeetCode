class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) in [0, 1]:
            return len(nums)
        
        # preIdx is the last index to be checked, next index is where to be inserted
        preIdx, nexIdx = 0, 1 # previous and next index
        cnt = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[preIdx]:
                continue
            nums[nexIdx] = nums[i]
            preIdx = nexIdx
            nexIdx = preIdx + 1
            cnt += 1 
        return cnt