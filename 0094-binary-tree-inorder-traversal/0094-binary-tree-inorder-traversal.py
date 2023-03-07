# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
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
                
        return traverse(root)