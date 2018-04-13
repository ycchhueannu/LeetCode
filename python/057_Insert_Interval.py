# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        
        ans = []
        
        # some boundary conditions
        if intervals == []:
            return [newInterval]
        elif newInterval.end < intervals[0].start:
            return [newInterval] + intervals
        elif newInterval.start > intervals[-1].end:
            return intervals + [newInterval]
        
        new_start = newInterval.start
        new_end = newInterval.end
        
        for i in range(0, len(intervals)):
            if intervals[i].end < new_start: # intertval[i].start <= interval[i].end < new_start
                ans.append(intervals[i])
            elif i and (intervals[i-1].end < new_start) and (new_end < intervals[i].start): # i >= 1
                ans += [newInterval] + intervals[i:]
                return ans
            else:
                merge_start = min(intervals[i].start, new_start)
                merge_end = max(intervals[i].end, new_end)
                break
                
        #print("i:", i)
        #print(merge_start, merge_end)
        
        notStop = 1
        for ii in range(i+1, len(intervals)):
            if intervals[ii].start > merge_end: # merge_start <= merge_end < intervals[ii].start
                notStop = 0
                break
        
        if notStop: # after traversing remaining intervals, merge_intvl overlaps the last (i.e. entire remaining) intervals
            merge_end = max(intervals[-1].end, merge_end) # or index ii
            ans.append(Interval(merge_start, merge_end))
            return ans

        merge_end = max(intervals[ii-1].end, merge_end)
        #print("ii:", ii)
        #print(merge_start, merge_end)
        ans.append(Interval(merge_start, merge_end))    
        
        ans += intervals[ii:]
        
        return ans