# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self, root):
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        diameter = [0]
        def dfs(root):
            if not root:
                return
            
            left = self.height(root.left)
            right = self.height(root.right)

            diameter[0] = max(diameter[0], left + right)
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return diameter[0]