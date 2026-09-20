class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0 for _ in range(numCourses)]
        adj = [[] for _ in range(numCourses)]
        
        for crs, pre in prerequisites:
            adj[pre].append(crs)
            indegree[crs] += 1
        
        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0: # course has no prereqs
                q.append(n)
        
        res = []
        finish = 0
        while q:
            crs = q.popleft()
            res.append(crs)
            finish += 1

            for pre in adj[crs]:
                indegree[pre] -= 1

                if indegree[pre] == 0:
                    q.append(pre)
        
        return [] if finish != numCourses else res


