# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def find_min(node):
            while node.left:
                node = node.left
            return node
        
        def delete_node(root, key):
            if not root:
                return root

            if key > root.val:
                root.right = delete_node(root.right, key)
            elif key < root.val:
                root.left = delete_node(root.left, key)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                else:
                    min_node = find_min(root.right)
                    root.val = min_node.val
                    root.right = delete_node(root.right, min_node.val)

            return root

        return delete_node(root, key)


