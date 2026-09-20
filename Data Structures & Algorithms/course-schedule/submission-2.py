class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # if we can find a topological sorting return true
        # if it fails it means the graph hasa cycle so we return false

        # 1. add nodes with an indegree of 0 to the queue
        # 2. visit nodes from the queue fifo
        # 3. delete all out going edges from this node
        # repeat steps 1 -> 3

        adj = { i: [] for i in range(numCourses)}

        for p, c in prerequisites:
            adj[p].append(c)
        
        print(adj)

        visit = set()

        def dfs(c):
            if c in visit:
                return False
            
            if adj[c] == []:
                return True
            
            visit.add(c)
            for p in adj[c]:
                if not dfs(p):
                    return False
            visit.remove(c)
            adj[c] = []
            return True


        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True
        
