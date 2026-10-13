class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list) # node -> list of (neighbor, weight)

        for u, v, t in times:
            adj[u].append((v, t))
        
        dist = {u: float('inf') for u in range(1, n + 1)}
        dist[k] = 0

        priority_queue = [(dist[k], k)] # key is total travel time

        while priority_queue:
            time, node = heapq.heappop(priority_queue)

            # no point in relaxing this edge it's not going to get smaller
            if time > dist[node]:
                continue

            for nei, weight in adj[node]:
                if time + weight < dist[nei]: # relax neighboring edges
                    dist[nei] = time + weight
                    heapq.heappush(priority_queue, (dist[nei], nei))
        print(dist)
        
        # 1 <-> 2 -> 3
        #   \-------/

        res = max(dist.values())
        return res if res != float('inf') else -1