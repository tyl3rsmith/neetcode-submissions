class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)

        for from_i, to_i in sorted(tickets)[::-1]: # lexicographically ordered
            adj[from_i].append(to_i)
        
        # Hierholzer’s Algorithm
        stack = ["JFK"]
        path = []

        while stack:
            curr = stack[-1]

            if not adj[curr]:
                path.append(stack.pop())
            else:
                stack.append(adj[curr].pop())

        return path[::-1]

        