# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        sum_ = 0
        def sumbst(root):
            nonlocal sum_
            if not root:
                return 
            sumbst(root.right)
            tmp = root.val
            root.val += sum_
            sum_ += tmp
            sumbst(root.left)
            

        sumbst(root)
        return root
            