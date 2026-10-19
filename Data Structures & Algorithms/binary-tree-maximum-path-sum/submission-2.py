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
        res = root.val

        # return max path sum without splitting
        def dfs(root):
            nonlocal res

            if not root:
                return 0
            
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # compute max path sum with a split
            maxPathSumSplit = root.val + leftMax + rightMax

            res = max(res, maxPathSumSplit)

            # return value without splitting
            maxPathSumNoSplit = root.val + max(leftMax, rightMax)

            return maxPathSumNoSplit

        dfs(root)
        return res

