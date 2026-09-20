"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        oldToNew = {}
        q = deque([node])
        copy = Node(node.val)
        oldToNew[node] = copy
        
        while q:
            curr = q.popleft()

            for neighbors in curr.neighbors:
                if neighbors not in oldToNew:
                    copy = Node(neighbors.val)
                    oldToNew[neighbors] = copy
                    q.append(neighbors)

                oldToNew[curr].neighbors.append(oldToNew[neighbors])

        return oldToNew[node]
