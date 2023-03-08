# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def merge(root1, root2):
            if not root1 and not root2:
                return None
            if not root1 and root2:
                value1 = 0
                value2 = root2.val
            if not root2 and root1:
                value1 = root1.val
                value2 = 0
            if root1 and root2:
                value1 = root1.val
                value2 = root2.val

            new_root = TreeNode(value1+value2)
            new_root.left = merge(root1.left if root1 else None, root2.left if root2 else None) 
            new_root.right = merge(root1.right if root1 else None, root2.right if root2 else None)

            return new_root
        return merge(root1, root2)