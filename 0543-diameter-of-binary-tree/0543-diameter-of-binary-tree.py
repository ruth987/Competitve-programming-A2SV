# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    
        diameter = []
        def height(root):
            if not root:
                return -1
            left = height(root.left)
            right = height(root.right)
            diameter.append(left+right+2)
            return max(left, right) + 1
        
        height(root)
        return max(diameter)
        
        
            
