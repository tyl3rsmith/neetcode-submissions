class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # input: array of intervals, interval = [start, end]
        # output: array of non overlapping intervals that have been merged
        # non-overlapping means no common point
        # guaranteed at least one interval
        
        # sort by the start time
        intervals.sort(key = lambda interval: interval[0])
        res = [intervals[0]]

        for start, end in intervals[1:]:
            if start <= res[-1][1]: # overlap
                res[-1][1] = max(end, res[-1][1])
            else:
                res.append([start, end])
                
        return res
          