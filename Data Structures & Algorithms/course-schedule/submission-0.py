class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:           
        graph = {}

        for i in range(numCourses):
            graph[i] = []
        
        for c, p in prerequisites:
            graph[c].append(p)
        
        visit = set()
        def dfs(i):
            if i in visit:
                return False

            if len(graph[i]) == 0:
                return True
            
            visit.add(i)

            for nei in graph[i]:
                if not dfs(nei):
                    return False
            
            visit.remove(i)
            graph[i] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
        print(graph)