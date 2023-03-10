# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        """
        we can traverse through all and store the elements and count number of occurence
        LPR
        """
        mydict = {}
        def traverse(root):
            if not root:
                return 
            if root.left:
                traverse(root.left)
                
            if root.val not in mydict:
                mydict[root.val] = 1
            else:
                mydict[root.val] += 1
                
            if root.right:
                traverse(root.right)
        
        traverse(root)
        mydict = sorted(mydict.items(), key = lambda item: -item[1])
        
        max_val = mydict[0][1]
        ans = []
        for key,val in mydict:
            if val == max_val:
                ans.append(key)
                
        return ans
            
            
            