# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        sum_ = 0
        def sumEvenG(root, parent, Gparent):
            nonlocal sum_
            if not root:
                return sum_
            
            if Gparent and Gparent.val % 2 == 0:
                sum_ += root.val
                
            Gparent = parent
            parent = root
            sumEvenG(root.left, parent, Gparent)
            sumEvenG(root.right, parent, Gparent)

        
        sumEvenG(root, None, None)
        return sum_
        
        
        