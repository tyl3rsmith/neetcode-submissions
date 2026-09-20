class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # input: array of intervals, interval = [start, end]
        # output: array of non overlapping intervals that have been merged
        # non-overlapping means no common point
        # guaranteed at least one interval

        # sort the interval by start time
        intervals.sort(key = lambda interval: interval[0])

        # guaranteed at least one interval
        res = [intervals[0]]

        for start, end in intervals:
            if start <= res[-1][1]:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([start, end])
        
        return res


        return res