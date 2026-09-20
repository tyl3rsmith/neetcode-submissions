class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for t in tasks:
            if t in count:
                count[t] += 1
            else:
                count[t] = 1

        maxHeap = []
        for t in count:
            maxHeap.append(-count[t])
        heapq.heapify(maxHeap)

        q = deque([])
        time = 0

        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append((cnt, time + n))
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time