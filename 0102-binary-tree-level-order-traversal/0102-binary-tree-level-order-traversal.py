# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        
        def traverse(root, val):
            if not root:
                return 
            if root.left:
                if val not in mydict:
                    mydict[val] = [root.left.val]
                else:
                    mydict[val].append(root.left.val)
                traverse(root.left, val+1)
            if root.right:
                if val not in mydict:
                    mydict[val] = [root.right.val]
                else:
                    mydict[val].append(root.right.val)
                traverse(root.right, val+1)

        mydict = {0:[root.val]}
        traverse(root, 1)
        ans = []
        for key,val in mydict.items():
            ans.append(val)
        
        return ans
            