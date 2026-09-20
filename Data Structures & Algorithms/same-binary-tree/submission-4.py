# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque([p])
        q2 = deque([q])

        while q1 and q2:
            n1 = q1.popleft()
            n2 = q2.popleft()

            if not n1 and not n2:
                continue
                
            if n1 and not n2:
                return False
            if n2 and not n1:
                return False
            if n1.val != n2.val:
                return False
            
            if n1.left:
                q1.append(n1.left)
                if not n2.left:
                    return False

            if n1.right:
                q1.append(n1.right)
                if not n2.right:
                    return False
            
            if n2.left:
                q2.append(n2.left)
                if not n1.left:
                    return False

            if n2.right:
                q2.append(n2.right)
                if not n1.right:
                    return False

        
        return True

            
        