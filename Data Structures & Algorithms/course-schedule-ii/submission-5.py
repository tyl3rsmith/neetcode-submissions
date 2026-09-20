class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseMap = {i:[] for i in range(numCourses)}
        indegree = [0 for _ in range(numCourses)]

        for crs, pre in prerequisites:
            courseMap[pre].append(crs)
            indegree[crs] += 1

        topSort = []

        visit = set()

        def dfs(crs):
            topSort.append(crs)
            indegree[crs] -= 1
            
            for pre in courseMap[crs]:
                indegree[pre] -= 1
                if indegree[pre] == 0:
                    dfs(pre)

        
        for crs in range(numCourses):
            if indegree[crs] == 0:
                dfs(crs)
        
        return topSort if len(topSort) == numCourses else []