"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events = []
        for interval in intervals:
            events.append((interval.start, 1)) # interval started
            events.append((interval.end, -1)) # interval ended
        
        events.sort()
        res = count = 0

        for t, e in events:
            count += e
            res = max(res, count)
        
        return res
