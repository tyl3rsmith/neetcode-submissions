class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int: 
        dist = {u: float('inf') for u in range(1, n + 1)}
        dist[k] = 0

        for _ in range(n - 1):
            for u, v, w in times:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        
        max_dist = max(dist.values())
        return max_dist if max_dist != float('inf') else -1

