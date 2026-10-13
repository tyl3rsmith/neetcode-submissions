class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for u, v, w in times:
            adj[u].append((v, w))
        
        dist = {i: float('inf') for i in range(1, n + 1)}

        def dfs(time, node):
            if time >= dist[node]:
                return

            dist[node] = time

            for nei, w in adj[node]:
                dfs(time + w, nei)
        
        dfs(0, k)
        res = max(dist.values())

        return res if res != float('inf') else -1
