class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # new interval goes before curr interval
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                # all the intervals after must be non overlapping
                for j in range(i, len(intervals)):
                    res.append(intervals[j])
                return res
            
            # new interval goes after curr interval
            elif intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
            
            # new interval is overlapping with curr interval
            else: 
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        res.append(newInterval)
        return res



        