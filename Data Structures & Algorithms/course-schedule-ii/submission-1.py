class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = { c:[] for c in range(numCourses)}

        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        
        # course has 3 states:

        # visited -> crs has been added to output
        # visiting -> crs not added to output but added to cycle
        # unvisited -> crs not added to output or cycle

        visit = set() # tells us if a node has been visited already
        cycle = set() # tells us if there is a cycle
        output = []

        def dfs(crs):
            if crs in cycle: # cycle detected
                return False

            if crs in visit: # dont need to rerun dfs on it
                return True
            
            cycle.add(crs)

            for pre in prereq[crs]:
                if not dfs(pre): # detected cycle
                    return False
            
            cycle.remove(crs) # no longer along the path we're exploring
            visit.add(crs) # we went through this crs and its prereqs
            output.append(crs)
            return True

        for n in range(numCourses):
            if not dfs(n):
                return []

        return output