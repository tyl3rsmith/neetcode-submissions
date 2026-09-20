class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            courseMap[pre].append(crs)
        

        cycle = set()
        def dfs(crs):
            # cycle detected
            if crs in cycle:
                return False
            
            # no pre-reqs
            if courseMap[crs] == []:
                return True
            
            cycle.add(crs)

            for pre in courseMap[crs]:
                if not dfs(pre):
                    return False # immediately return false if we have a cycle
            
            cycle.remove(crs) # done exploring this path
            
            return True


        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True


