# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int: 
        res = 1
        def dfs(curr, curr_max):
            nonlocal res

            if not curr:
                return

            if curr.left:
                if curr.left.val >= curr_max:
                    res += 1
                dfs(curr.left, max(curr_max, curr.left.val))

            if curr.right:
                if curr.right.val >= curr_max:
                    res += 1
                dfs(curr.right, max(curr_max, curr.right.val))
        
        dfs(root, root.val)
        return res