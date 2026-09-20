class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        minHeap = []
        res = {}
        i = 0
        for q in sorted(queries):

            # this query falls in these intervals
            # we know it falls in the interval if it starts before this query
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                # in cases of a tie we pop the interval that came first
                # i.e. the one with a smaller end time (r) is popped first
                heapq.heappush(minHeap, (r - l + 1, r))
                i += 1
            
            # if intervals are out of bounds i.e. r < q i.e. they ended 
            # before this one started we remove them from the heap as they
            # are out of consideration since the query doesn't fall in
            # this interval
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)

            res[q] = minHeap[0][0] if minHeap else -1
        
        return [res[q] for q in queries]

