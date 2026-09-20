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
        
        clone = {}
        
        q = deque([node])
        copy = Node(node.val)
        clone[node] = copy

        while q:
            curr = q.popleft()

            for nei in curr.neighbors:
                if nei not in clone:
                    copy = Node(nei.val)
                    clone[nei] = copy
                    q.append(nei)
                
                clone[nei].neighbors.append(clone[curr])
        
        return clone[node]