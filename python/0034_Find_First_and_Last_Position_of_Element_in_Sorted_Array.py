class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def get_min_idx(high):
            low = 0
            tmp_min = -1
            is_in_next_recursive = False
            #print("in get_min, nums:", nums[:high+1])
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    #print("find mid", mid)
                    tmp_min = get_min_idx(mid-1)
                    is_in_next_recursive = True
                    #print("tmp_min", tmp_min)
                    break
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            if is_in_next_recursive and tmp_min == -1:
                #print("return:", mid)
                return mid
            return tmp_min
        
        def get_max_idx(low):
            high = len(nums) - 1
            tmp_max = -1
            is_in_next_recursive = False
            #print("in get_max, nums:", nums[low:])
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    #print("find mid", mid)
                    tmp_max = get_max_idx(mid+1)
                    is_in_next_recursive = True
                    #print("tmp_max", tmp_max)
                    break
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            if is_in_next_recursive and tmp_max == -1:
                #print("return:", mid)
                return mid
            return tmp_max
        
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                min_idx = get_min_idx(mid)
                max_idx = get_max_idx(mid)
                return [min_idx, max_idx]
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return [-1, -1]