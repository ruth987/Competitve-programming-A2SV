# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        averages = []
        def bfs(root):
            qu = deque([root])
            
            while qu:
                total = 0
                length = len(qu)

                for i in range(length):
                    node = qu.popleft()
                    total += node.val

                    if node.left:
                        qu.append(node.left)
                    if node.right:
                        qu.append(node.right)

                averages.append(total/length)
                
        bfs(root)
        return averages