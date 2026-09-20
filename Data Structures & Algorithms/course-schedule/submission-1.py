class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # if we can find a topological sorting return true
        # if it fails it means the graph hasa cycle so we return false

        # 1. add nodes with an indegree of 0 to the queue
        # 2. visit nodes from the queue fifo
        # 3. delete all out going edges from this node
        # repeat steps 1 -> 3

        indegree = [0] * numCourses
        adj = [[] for x in range(numCourses)]
        
        for course, prereq in prerequisites:
            indegree[prereq] += 1
            adj[course].append(prereq)
        
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        finish = 0
        res = ""
        while queue:
            node = queue.popleft()
            finish += 1
            res += f"{node}, "

            for nei in adj[node]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    queue.append(nei)
        
        print(res)
        return finish == numCourses

            