class DisjointSetUnion:
    def __init__(self, n):
        self.Parent = list(range(n + 1)) # parent of each node for tree structure
        self.Size = [1] * (n + 1) # keeps track of size of each node so we can union by rank

    def find(self, x):
        if self.Parent[x] != x:
            self.Parent[x] = self.find(self.Parent[x]) # path compressing 

        return self.Parent[x]
        
    
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)

        if rx == ry:
            return False

        # merging y into x
        # if y is larger swap the trees
        # union by size
        if self.Size[ry] > self.Size[rx]:
            rx, ry = ry, rx
        
        self.Parent[ry] = rx # merge y into x
        self.Size[rx] += self.Size[ry]
        
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # kruskals algorithm

        # sort the edges in inc order
        # stores dist between every possible pair of edges min cost is at the top
        minHeap = [] # key = dist

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                xi, yi = points[i]
                xj, yj = points[j]

                dist = abs(xi - xj) + abs(yi - yj)
                heapq.heappush(minHeap, (dist, i, j))
        
        # initialize DSU
        n = len(points)
        DSU = DisjointSetUnion(n)


        total_cost = 0

        while minHeap:
            cost, i, j = heapq.heappop(minHeap)
            if DSU.union(i, j): # edge connects two seperate points
                total_cost += cost

        return total_cost
        