# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        deq = deque([root])
        
        while deq:
            rightside = None
            deq_len = len(deq)
            
            for i in range(deq_len):
                node = deq.popleft()
                
                if node:
                    rightside = node
                    deq.append(node.left)
                    deq.append(node.right)
                    
            if rightside:
                ans.append(rightside.val)
                    
        return ans
                
                
            