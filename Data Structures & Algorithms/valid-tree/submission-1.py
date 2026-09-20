class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i:[] for i in range(n)}

        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
        
        visit = set()
        count = 0

        def dfs(node, parent):
            nonlocal count
            count += 1
            
            if node in visit:
                return False
            
            visit.add(node)

            for nei in adj[node]:

                if nei == parent:
                    continue
                
                if not dfs(nei, node):
                    return False

            return True

        good = dfs(0, -1)
        return good and count == n

            
        