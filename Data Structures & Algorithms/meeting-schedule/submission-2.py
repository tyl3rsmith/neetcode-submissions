"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        n = len(intervals)
        for i in range(n):
            for j in range(i + 1, n):
                i1 = intervals[i]
                i2 = intervals[j]

                if min(i1.end, i2.end) > max(i1.start, i2.start):
                    return False
        
        return True


