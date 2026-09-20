"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {}

        def dfs(source):
            # base case: node was already cloned
            if source in old_to_new:
                return old_to_new[source]

            # if not we need to clone it
            old_to_new[source] = Node(source.val, [])

            # clone the neighbors
            for neighbor in source.neighbors:
                old_to_new[source].neighbors.append(dfs(neighbor))
            
            return old_to_new[source]
        
        return dfs(node) if node else None
