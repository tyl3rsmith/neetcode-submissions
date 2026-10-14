class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int: 
        dist = {u: {v: float('inf') for v in range(1, n + 1)} for u in range(1, n + 1)}
        
        # initialize distance to self to be 0
        for i in range(1, n + 1):
            dist[i][i] = 0

        # initialize direct distances
        for u, v, w in times:
            dist[u][v] = w
        
        # would going from u to v through m be shorter than the best curr distance
        for m in range(1, n + 1):
            for u in range(1, n + 1):
                for v in range(1, n + 1):
                    dist[u][v] = min(dist[u][v], dist[u][m] + dist[m][v])
        
        res = max(dist[k].values())

        return res if res != float('inf') else -1
