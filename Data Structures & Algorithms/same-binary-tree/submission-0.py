# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def bfs(root):
            queue = deque([root])
            res = {}
            
            i = 0
            while queue:
                node = queue.popleft()
                if node:
                    res[i] = node.val
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    res[i] = 'null'

                i += 1
            
            print(res)
            return res
        
        return bfs(p) == bfs(q)

        