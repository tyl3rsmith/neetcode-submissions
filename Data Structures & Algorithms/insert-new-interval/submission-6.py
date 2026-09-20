class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        i = 0
        res = []
        
        # new interval comes after this interval
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        
        # new interval comes before this one
        # check if we have to merge
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            i += 1

        # new interval goes here
        res.append(newInterval)

        # add remaining intervals after the last merge occurred
        while i < n:
            res.append(intervals[i])
            i += 1

        return res        
