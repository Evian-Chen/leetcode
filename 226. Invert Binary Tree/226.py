# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        else:
            old_r = self.invertTree(root.right)
            old_l = self.invertTree(root.left)

            if old_l is not None:
                new_r = TreeNode(val=old_l.val, left=old_l.left, right=old_l.right)
            else:
                new_r = None
            
            if old_r is not None:
                new_l = TreeNode(val=old_r.val, left=old_r.left, right=old_r.right)
            else:
                new_l = None

            root.right = new_r
            root.left = new_l

            return root
