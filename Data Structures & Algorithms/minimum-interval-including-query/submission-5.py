class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        events = []
        for i in range(len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            events.append((start, 0, end - start + 1, i))
            events.append((end, 2, end - start + 1, i))
        
        for i in range(len(queries)):
            events.append((queries[i], 1, i))
        
        events.sort(key = lambda e: (e[0], e[1]))

        minSizes = []
        inactiveIntervals = [False] * len(intervals) # lazy deletion only delete invalid ones at the top of the heap
        res = [-1] * len(queries)

        for time, type, *rest in events:
            if type == 0: # start
                interval_length, idx = rest
                heapq.heappush(minSizes, (interval_length, idx))
            elif type == 1: # query
                query_idx = rest[0]
                while minSizes and inactiveIntervals[minSizes[0][1]]:
                    heapq.heappop(minSizes)

                if minSizes:
                    res[query_idx] = minSizes[0][0]

            else: # end
                idx = rest[1]
                inactiveIntervals[idx] = True
        
        return res