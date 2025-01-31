# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root.left, root.right)

    def helper(self, l, r):
        if l is None and r is None:
            return True
        elif l is not None and r is not None:
            if r.val == l.val:
                return self.helper(l.right, r.left) and self.helper(l.left, r.right)
            else:
                return False
        else:
            return False