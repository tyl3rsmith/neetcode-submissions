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
            return
        
        conversion_table = {}
        queue = deque([node])
        conversion_table[node] = Node(node.val)

        while queue:
            curr = queue.popleft()

            for neighbor in curr.neighbors:
                if neighbor not in conversion_table:
                    conversion_table[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                conversion_table[curr].neighbors.append(conversion_table[neighbor])

        return conversion_table[node]
        
            

