class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)

        # reverse lexicographical order since we always pop from the end
        # the element at the end needs to be the lexicographically smallest one
        for src, dst in sorted(tickets)[::-1]:
            adj[src].append(dst)
        
        print(sorted(tickets)[::-1])
        print(adj)

        res = []
        def dfs(src):
            while adj[src]: # still have neighbors to explore
                dst = adj[src].pop() # explore this neighbor and remove from consideration
                dfs(dst)
            
            # adding node only when no more outgoing edges
            res.append(src)

        dfs('JFK') # always starting at jfk

        return res[::-1] # reverse the path since dfs was postorder