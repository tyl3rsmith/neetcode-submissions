class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # greedy: sort by start value
        intervals.sort(key = lambda i: i[0])
        print(intervals)

        res = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            # no overlap
            if start >= prevEnd:
                prevEnd = end
            else: # overlap start <= prevEnd
                # greedily remove the interval that ends later
                prevEnd = min(prevEnd, end)
                res += 1
        
        return res
