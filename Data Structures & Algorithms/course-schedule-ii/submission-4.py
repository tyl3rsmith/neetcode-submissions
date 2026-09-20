class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseMap = {i:[] for i in range(numCourses)}
        indegree = [0 for _ in range(numCourses)]

        for crs, pre in prerequisites:
            courseMap[crs].append(pre)
            indegree[pre] += 1
        
        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)
        
        topSort = []
        finish = 0
        while q:
            pre = q.popleft()
            topSort.append(pre)
            finish += 1

            for crs in courseMap[pre]:
                indegree[crs] -= 1
                if indegree[crs] == 0:
                    q.append(crs)

        return topSort[::-1] if finish == numCourses else []