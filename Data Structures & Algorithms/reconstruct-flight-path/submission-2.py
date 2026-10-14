class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for s, e in tickets:
            heapq.heappush(graph[s], e)

        print(graph)
        
        path = []

        def dfs(node):
            while graph[node]: # visit all neighbors
                dfs(heapq.heappop(graph[node])) # once we visit we pop so we never revisit it
            
            path.append(node) # no more neighbors to visit add it to solution
        
        dfs("JFK")
        path.reverse() # post order dfs so need to reverse the path

        return path



        