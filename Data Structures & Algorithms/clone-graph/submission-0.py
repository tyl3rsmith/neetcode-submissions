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
        
        table = {}
        queue = deque([node])
        table[node] = Node(node.val)

        while queue:
            curr = queue.popleft()

            for neighbor in curr.neighbors:
                if neighbor not in table:
                    table[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                table[curr].neighbors.append(table[neighbor])
        
        return table[node]
            

