class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}

        for c, p in prerequisites:
            adj[c].append(p)
        
        print(adj)

        visit = set()
        def dfs(c):
            # cycle detected
            if c in visit:
                return False
            
            if adj[c] == []:
                return True

            visit.add(c)
            for pre in adj[c]:
                if not dfs(pre):
                    return False
            visit.remove(c)

            adj[c] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
            
        return True
