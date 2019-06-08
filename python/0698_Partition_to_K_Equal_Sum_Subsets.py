class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k == 1:
            return True
        elif k > len(nums):
            return False
        total = sum(nums)
        if total % k != 0:
            return False
        ave = total // k
        
        nums.sort(reverse=True)
        if nums[0] > ave: # since nums[i] > 0
            return False
        
        def DFS(not_visit, bi, bucket):
            if bi == len(bucket):
                return True
            elif bucket[bi] == 0:
                if DFS(not_visit, bi+1, bucket):
                    return True
                return False
        
            for i in range(0, len(nums)):
                if not_visit[i] and bucket[bi] >= nums[i]:
                    not_visit[i] = False
                    bucket[bi] -= nums[i]
                    if DFS(not_visit, bi, bucket):
                        return True
                    else: # reset
                        bucket[bi] += nums[i]
                        not_visit[i] = True
            return False
        
        # args: not_visit, index of bucket, bucket (k subsets)
        return DFS([True]*len(nums), 0, [ave]*k)