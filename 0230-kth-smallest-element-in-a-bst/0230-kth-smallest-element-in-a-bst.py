# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        inorder traverse :LPR
        """
        ans = []
        def traverse(root):
            if not root:
                return ans
            if root.left:
                traverse(root.left)
            ans.append(root.val)
            if root.right:
                traverse(root.right)
            return ans
        
        traverse(root)
        return ans[k-1]
    