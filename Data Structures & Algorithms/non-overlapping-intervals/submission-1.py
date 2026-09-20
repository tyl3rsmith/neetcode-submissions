class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by the start value
        intervals.sort(key = lambda i: i[0])
        res = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            # overlapping interval
            if start < prevEnd:
                res += 1
                prevEnd = min(prevEnd, end)
            
            # no overlap
            else:
                prevEnd = end
        
        return res

        