class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def DFS(i):
            if nums[i] == i+1 or nums[i] == nums[nums[i]-1]:
                return
            nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
            DFS(i)
            return
        
        ret = []
        for i in range(len(nums)):
            DFS(i)
        
        for i in range(len(nums)):
            if nums[i] - 1 != i:
                ret.append(i+1)
        
        return ret