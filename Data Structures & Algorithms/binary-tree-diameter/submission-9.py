# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root, diameter):
        if not root:
            return 0 # height
        
        leftHeight = self.dfs(root.left, diameter)
        rightHeight = self.dfs(root.right, diameter)

        diameter[0] = max(diameter[0], leftHeight + rightHeight)
        return 1 + max(leftHeight, rightHeight)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0]
        self.dfs(root, diameter)
        return diameter[0]
