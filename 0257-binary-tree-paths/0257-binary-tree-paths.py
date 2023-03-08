# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        """
        preorder traversing - PLR
        """
        def binaryTrees(root, astr, ans):
            if not root:
                return 
            if not root.left and not root.right:
                astr += str(root.val)
                ans.append(astr)
            astr += (str(root.val) + "->")
            binaryTrees(root.left, astr, ans)
            binaryTrees(root.right, astr, ans)

            return ans
            
        
        return binaryTrees(root, "", [])
    