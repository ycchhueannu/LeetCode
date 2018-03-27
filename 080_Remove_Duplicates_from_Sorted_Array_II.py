class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        
        # preIdx is the last index to be checked, next index is where to be inserted
        preIdx, nexIdx = 0, 1 # previous and next index
        cnt = 1
        dup = 0
        for i, val in enumerate(nums[1:]):
            if val == nums[preIdx]:
                if not dup:
                    nums[nexIdx] = val
                    preIdx = nexIdx
                    nexIdx = preIdx + 1
                    cnt += 1
                    dup = 1
                continue
                
            nums[nexIdx] = val
            preIdx = nexIdx
            nexIdx = preIdx + 1
            cnt += 1
            dup = 0
        return cnt


"""
i = 0
    for n in nums:
        if i < 2 or n > nums[i-2]:
            nums[i] = n
            i += 1
    return i
"""