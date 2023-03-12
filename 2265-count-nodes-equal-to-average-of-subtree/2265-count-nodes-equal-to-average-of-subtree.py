# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:

        sum_ = 0
        count = 0
        def subtree_sum(root):
            nonlocal sum_, count
            if not root:
                return 
            
            sum_ += root.val
            count += 1
            if root.left:
                subtree_sum(root.left)
            if root.right:
                subtree_sum(root.right)
          
        ans = 0
        def check(root):
            nonlocal ans, sum_, count
            if not root:
                return
            
            sum_, count = 0, 0
            subtree_sum(root)
            if count != 0 and root.val == (sum_)//count:
                ans += 1
                
            check(root.left)
            check(root.right)
        
        check(root)
        return ans