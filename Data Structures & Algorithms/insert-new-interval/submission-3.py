class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            # new interval comes before current interval
            # if end is before the start of the current interval
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                for j in range(i, len(intervals)):
                    res.append(intervals[j])
                return res
            
            # starts after the current one ends
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            
            # overlapping interval
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]), 
                    max(newInterval[1], intervals[i][1])
                ]

        res.append(newInterval)
        return res

        


        