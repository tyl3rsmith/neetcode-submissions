class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        topSort = []

        visit = set()
        cycle = set()

        def dfs(crs):
            if crs in cycle:
                return False
            
            if crs in visit:
                return True
            
            if preMap[crs] == []: # no pre-reqs
                topSort.append(crs)
                visit.add(crs)
                return True
            
            cycle.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): # cycle detected
                    return False
            
            cycle.remove(crs)
            visit.add(crs)
            topSort.append(crs)
            return True # no more neighbors to process
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return topSort