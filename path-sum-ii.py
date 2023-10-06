# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        
        def dfs(root, sum_, path):
            if not root:
                return 
            if not root.left and not root.right:
                # print(sum_)
                if sum_+root.val == targetSum:
                    ans.append(path+[root.val])
                return 

            dfs(root.left, sum_ + root.val, path+[root.val])
            dfs(root.right, sum_ + root.val, path+[root.val])
        
        dfs(root, 0, [])
        return ans