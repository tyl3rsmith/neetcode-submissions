# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # the val in preorder tells us the root
    # inorder tells us whats in the left and right sub tree

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val: idx for idx, val in enumerate(inorder)}

        pre_idx = 0
        in_idx = 0

        def dfs(limit):
            nonlocal pre_idx, in_idx

            if pre_idx >= len(preorder):
                return None
            
            if inorder[in_idx] == limit:
                in_idx += 1
                return None

            root_val = preorder[pre_idx]
            root = TreeNode(root_val)
            pre_idx += 1

            root.left = dfs(root_val)
            root.right = dfs(limit)

            return root

        return dfs(float('inf'))