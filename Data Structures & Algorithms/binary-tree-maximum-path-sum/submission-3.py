# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# if root < 0: max(left, right)
# if root > 0: max(root + left, root + right)

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0, float("-inf")

            leftNoSplit, leftBest = dfs(node.left)
            rightNoSplit, rightBest = dfs(node.right)

            # Ignore negative contributions from children
            left = max(0, leftNoSplit)
            right = max(0, rightNoSplit)

            # Best path starting at this node, extendable upward
            noSplit = node.val + max(left, right)

            # Best path that passes through this node using both sides
            throughNode = node.val + left + right

            # Best complete path anywhere in this subtree
            withSplit = max(
                throughNode,
                leftBest,
                rightBest
            )

            return noSplit, withSplit

        return dfs(root)[1]