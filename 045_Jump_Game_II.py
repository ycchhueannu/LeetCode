from itertools import compress
class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        step_list = [0] * len(nums) # assume last index is reachable
        notVisit = [1] * len(nums)
        traverse_list = [0] # start node, at index 0
        while traverse_list != []:
            i = traverse_list[0]
            print("traverse list:", traverse_list, "nums[i]:",nums[i])
            for cur_step in list( filter( lambda x: x < len(nums), compress( map(lambda x: i + x, range(1, nums[i]+1)) , \
                                                                   notVisit[i+1:i+nums[i]+1] ) ) )[::-1]:
                #print("cur step:", cur_step)
                if cur_step == len(nums) - 1:
                    return step_list[i] + 1
                else:
                    step_list[cur_step] = step_list[i] + 1
                    traverse_list.append(cur_step)
                    notVisit[cur_step] = 0
            del traverse_list[0] # note that 'del i' will not affect traverse_list

"""
line 16:
for step in range(1, nums[i]+1): # 1 ~ nums[i] steps
    cur_step = i + step
"""