class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # prioritize the more frequent tasks
        count = {}
        for t in tasks:
            if t in count:
                count[t] += 1
            else:
                count[t] = 1
        
        maxHeap = []
        queue = deque([])

        for t in count:
            maxHeap.append(-count[t])
        heapq.heapify(maxHeap)

        time = 0

        while maxHeap or queue:
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    queue.append((cnt, time + n))
                
            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])

        return time