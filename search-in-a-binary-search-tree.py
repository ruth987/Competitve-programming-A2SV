# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def search(root, val):
            if root and root.val > val:
                return self.searchBST(root.left, val)
            elif root and root.val < val:
                return self.searchBST(root.right, val)
            return root
                
        return search(root, val)