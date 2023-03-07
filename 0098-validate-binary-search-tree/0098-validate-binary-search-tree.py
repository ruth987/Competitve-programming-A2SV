# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # do the inorder traverse (LPR)
        def inorder(root):
            left, right = [], []
            
            if not root:
                return []
            if root.left:
                left = inorder(root.left)
            if root.right:
                right = inorder(root.right)

            return left+[root.val]+right
        
        ans = inorder(root)
        if len(set(ans)) != len(ans):
            return False
        return ans == sorted(ans)