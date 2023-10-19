# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        count = 0
        def findamount(root):
            nonlocal count
            if not root:
                return 0

            left = findamount(root.left)
            right = findamount(root.right)

            count += (abs(left) + abs(right)) 

            return left+right+root.val-1


        findamount(root)
        return count