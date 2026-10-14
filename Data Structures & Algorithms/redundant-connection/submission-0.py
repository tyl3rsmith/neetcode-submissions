class Solution:
    def isCycle(self, edges: List[List[int]]) -> bool:
        visited = set()
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node, parent):
            visited.add(node)

            for nei in adj[node]:
                if nei not in visited: # neighbor hasn't been visited
                    if dfs(nei, node):
                        return True

                # neighbor already been visited and it's not the parent -> there's a cycle
                elif nei in visited and nei != parent:
                # if nei == parent it means we came from this node in the undirected graph
                    return True

        if dfs(edges[0][0], -1):
            return True
        else:
            return False

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # brute force delete every edge and see if there's still a cycle
        edges.reverse()
        
        # for deleted edge 1, 2,.., n:
        #     try the rest of the edges:
        #         if there is a cycle:
        #             skip and try a different deleted edge
        #         if there is not a cycle
        #             return the deleted edge
        print(edges)

        for i in range(len(edges)):
            deleted_edge = edges[i]
            new_edges = []
            for j in range(len(edges)):
                if j == i:
                    continue
                new_edges.append(edges[j])
            
            if self.isCycle(new_edges):
                continue
            else:
                return deleted_edge

