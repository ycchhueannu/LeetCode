class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k <= 0:
            return False
        if k < len(nums):
            end = k
        else:
            end = len(nums)-1
        d = {} # num: idx
        for i in range(0, end+1):
            ni = nums[i]
            if ni not in d:
                d[ni] = i
            elif i - d[ni] > k:
                d[ni] = i
            else:
                return True
            
        for i in range(end+1, len(nums)):
            ni = nums[i]
            if ni not in d:
                d[ni] = i
            elif i - d[ni] > k:
                d[ni] = i
            else:
                return True
            
        return False