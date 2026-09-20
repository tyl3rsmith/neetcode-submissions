class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        events = []
        # 3 events: start, query, end in that order
        for i in range(len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            # (time, type, length, location)
            events.append((start, 0, end - start + 1, i))      
            events.append((end, 2, end - start + 1, i))  
        
        for i in range(len(queries)):
            # (query, type, location)
            events.append((queries[i], 1, i))
        
        # sort by time and type (we query before we end)
        events.sort()

        print(events)

        minHeap = [] # (size, index)
        res = [-1] * len(queries)
        inactive = [False] * len(intervals)

        for time, type, *rest in events:
            if type == 0: # start
                interval_size, idx = rest
                heapq.heappush(minHeap, (interval_size, idx))
            elif type == 2: # end
                idx = rest[1]
                inactive[idx] = True
            else: # query
                query_idx = rest[0]
                while minHeap and inactive[minHeap[0][1]]:
                    heapq.heappop(minHeap)
                
                if minHeap:
                    res[query_idx] = minHeap[0][0]
        return res