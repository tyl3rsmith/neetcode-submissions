class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = {i:[] for i in range(numCourses)}
        indegree = [0 for _ in range(numCourses)]

        for crs, pre in prerequisites:
            courseMap[pre].append(crs)
            indegree[crs] += 1
        
        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        count = 0

        while q:
            pre = q.popleft()
            count += 1

            for crs in courseMap[pre]:
                indegree[crs] -= 1

                if indegree[crs] == 0:
                    q.append(crs)
        
        return count == numCourses

