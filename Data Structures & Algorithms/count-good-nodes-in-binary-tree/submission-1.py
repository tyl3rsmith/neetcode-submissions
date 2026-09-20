# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int: 
        def dfs(curr, curr_max):
            if not curr:
                return 0
            
            if curr.val >= curr_max:
                return 1 + dfs(curr.left, curr.val) + dfs(curr.right, curr.val)
            else:
                return dfs(curr.left, curr_max) + dfs(curr.right, curr_max)
        
        return dfs(root, root.val)