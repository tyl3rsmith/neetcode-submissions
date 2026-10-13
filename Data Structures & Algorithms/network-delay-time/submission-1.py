class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = {}

        for i in range(1, n + 1):
            edges[i] = []

        for u, v, w in times:
            edges[u].append((v, w))
        
        dist = {node: float("inf") for node in range(1, n + 1)}

        print(dist)
        print(edges)

        def dfs(node, time):
            if time >= dist[node]:
                return

            dist[node] = time
            for nei, w in edges[node]:
                dfs(nei, time + w)
        
        dfs(k, 0)
        res = max(dist.values())

        return res if res != float('inf') else -1
        