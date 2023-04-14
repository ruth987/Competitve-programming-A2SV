# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        we can do a dfs and store all the members in different lists which 
        we can call a path and use it as a parameter
        """
        allPaths = []
        path = []
        sum_ = 0
        total = 0
        def dfs(root):
            nonlocal sum_,total
    
            if not root:
                return

            if total:
                total *= 10
            total += root.val
            
            if not root.left and not root.right:
                sum_ += total
                total //= 10
                return 
            
            dfs(root.left)
            dfs(root.right)
            total //= 10

        dfs(root)
        return sum_