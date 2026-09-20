"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(node):
            if node in oldToNew: # already cloned
                return oldToNew[node]
            else: # clone it
                clone = Node(node.val)
                oldToNew[node] = clone

                for neighbor in node.neighbors:
                    clone.neighbors.append(dfs(neighbor)) # clone its neighbors
                
                return clone
        
        return dfs(node) if node else None
