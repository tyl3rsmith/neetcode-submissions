class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        events = []
        # two events: interval starts, interval ends
        # first priority is the time the event occurred
        # second priority is the type start has priority over end

        for start, end in intervals:
            events.append([start, -1])
            events.append([end, 1])
        
        events.sort(key = lambda i: (i[0], i[1]))

        started = 0
        res = []
        interval = [float('inf'), -1]

        for e, t in events:
            if t == -1: # start event
                started += 1
                interval[0] = min(interval[0], e)
            else: # end event
                started -= 1
                # no overlaps we can close interval and add to res
                if started == 0:
                    interval[1] = e
                    res.append(interval)
                    interval = [float('inf'), -1] # reset for next iteration

        
        return res