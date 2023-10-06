# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        """
        i start from the root of both the trees then i compair their left side
        if it is not the same:
            swap it
            still not the same:
                return False
        else:
            keep compairing the rest of the trees
        """
        def isMatch(root1, root2):
            if not root1 and not root2:
                return True

            if not root1 or not root2:
                return False

            if root1.val != root2.val:
                return False

            #case 1: no flip needed
            if isMatch(root1.left, root2.left) and isMatch(root1.right,root2.right):
                return True
            
            #case 2: flip needed
            if isMatch(root1.left,root2.right) and isMatch(root1.right,root2.left):
                return True
            return False

        return isMatch(root1, root2)