class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        while val in nums:
            nums.remove(val)
        return len(nums)
        
        """
        if nums == []:
            return 0
            
        num_val = nums.count(val)
        if num_val == 0:
            return len(nums)
        
        
        
        st_idx = nums.index(val)
        cnt = 0

        for i in range(st_idx, len(nums)):
            #print("(i, nums[i]) = ({}, {})".format(i, nums[i]))
            if nums[i] == val:
                while nums[-1] == val:
                    del nums[-1]
                    cnt += 1
                    if cnt == num_val:
                        return len(nums)
                
                nums[i] = nums[-1]
                del nums[-1]
                cnt += 1
                
                if cnt == num_val:
                    return len(nums)

        """