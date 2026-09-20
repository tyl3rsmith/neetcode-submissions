class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            # goes before this interval
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)

                # add the remaining intervals
                for j in range(i, len(intervals)):
                    res.append(intervals[j])
                
                return res

            # goes after this interval
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])

            # must be merged
            else:
                newInterval = [min(newInterval[0], intervals[i][0]),
                               max(newInterval[1], intervals[i][1])
                ]
            
        res.append(newInterval)
        return res