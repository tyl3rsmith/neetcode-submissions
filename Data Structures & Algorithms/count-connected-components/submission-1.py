class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        def dfs(node, parent):
            if node in visit:
                return
            
            visit.add(node)
            for nei in adj[node]:
                if nei == parent:
                    continue
                
                dfs(nei, node)


        count = 0
        for i in range(n):
            if i in visit:
                continue
            
            count += 1
            dfs(i, -1)

        return count
            