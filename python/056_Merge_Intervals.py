# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if intervals == []:
            return []
        
        intervals.sort(key=lambda x: x.start)
        
        ans = []
        merge_start = intervals[0].start
        merge_end = intervals[0].end
        for intvl in intervals:
            if intvl.start > merge_end:
                ans.append(Interval(merge_start, merge_end))
                merge_start = intvl.start
                merge_end = intvl.end
            elif merge_end < intvl.end:
                merge_end = intvl.end

        ans.append(Interval(merge_start, merge_end))
        
        
        return ans