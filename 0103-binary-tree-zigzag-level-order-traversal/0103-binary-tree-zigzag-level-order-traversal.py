# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        mydict = {}
        def calc_depth(root, dep):
            if not root:
                return 
            
            if dep in mydict:
                mydict[dep].append(root.val)
            else:
                mydict[dep] = [root.val]

            left = calc_depth(root.left, dep+1)
            right = calc_depth(root.right, dep+1)
            
        calc_depth(root, 0)
        ans = []
                
        for key,val in mydict.items():
            if key%2 != 0:
                val = val[::-1]
            ans.append(val)
        return ans
                