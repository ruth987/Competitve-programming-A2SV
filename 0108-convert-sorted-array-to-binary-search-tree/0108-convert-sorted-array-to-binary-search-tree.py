# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def form(nums, left, right):

            mid = (left+right)//2
            if left <= right:
                return TreeNode(nums[mid], form(nums, left, mid-1), form(nums, mid+1, right))
            
        return form(nums,0, len(nums)-1)



