class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            graph[crs].append(pre)
        
        visit = set()
        def dfs(crs):
            # base case: course has already been seen, cycle detected
            if crs in visit:
                return False

            # base case: course has no pre-reqs
            if len(graph[crs]) == 0:
                return True
            
            visit.add(crs)
            for pre in graph[crs]:
                if not dfs(pre):
                    return False
            graph[crs] = []
            visit.remove(crs)
            return True
        

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True
