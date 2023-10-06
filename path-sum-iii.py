# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
        to calculate every path possibilities we can do dfs for each node 
        considering the two conditions:
            - if i keep going with the past node
            - if i start from that root node
        """
        
        def dfs(root, sum_):
            if not root:
                return 0

            count = 0
            if root.val == sum_: 
                count += 1

            count += dfs(root.left, sum_ - root.val) + dfs(root.right, sum_ - root.val)
            return count
        
        if not root:
            return 0

        return self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum) + dfs(root, targetSum)