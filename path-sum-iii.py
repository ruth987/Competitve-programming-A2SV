# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        total = 0
        def helper(root, curr):
            nonlocal total
            if not root:
                return
            helper(root.left, curr+root.val)
            helper(root.right, curr+root.val)
            if curr+root.val == targetSum:
                total += 1

        def dfs(root):
            if not root:
                return 
            helper(root, 0)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return total