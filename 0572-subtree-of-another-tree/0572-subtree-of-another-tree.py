# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def check(root1, root2):
            if not root1 and not root2:
                return True
            if (root1 and not root2) or (root2 and not root1):
                return False
            elif root1.val != root2.val:
                return False
            
            left = check(root1.left, root2.left)
            right = check(root1.right, root2.right)
            
            return (left and right)
        
        def searchSub(root, key):
            if not root:
                return False
            if root.val == key:
                val = check(root, subRoot)
                # print(val)
                if val:
                    return val
            left = searchSub(root.left, key)
            right = searchSub(root.right, key)
            return (left or right)
            

        return (searchSub(root, subRoot.val))
        