# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        """
        root, left, right
        do the operation for left then pop empty parenthesis
        do the operation for the right then pop empty parenthesis
        """
        ans = []
        def helper(root):
            nonlocal ans
            if not root:
                return ""

            left = helper(root.left)
            right = helper(root.right)
            
            if left == "" and right == "":
                return str(root.val)
            elif left == "":
                return str(root.val) + "()" + "(" + right + ")"
            elif right == "":
                return str(root.val) + "(" + left + ")"
            else:
                return str(root.val) + "(" + left + ")" + "(" + right + ")"
        
        ans = helper(root)
        return ans