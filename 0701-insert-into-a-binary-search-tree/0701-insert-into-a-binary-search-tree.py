# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val, None, None)

        def insert(root, val):
            if val > root.val:
                if not root.right:
                    root.right = TreeNode(val, None, None)
                    return root
                return insert(root.right, val)
            
            else: 
                if not root.left:
                    root.left = TreeNode(val, None, None)
                    return root
                return insert(root.left, val)
                
        insert(root, val)
        return root
    
    