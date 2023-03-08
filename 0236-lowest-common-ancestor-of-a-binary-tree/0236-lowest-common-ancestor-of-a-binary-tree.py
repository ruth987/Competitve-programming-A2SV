# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        let's try to find the parents of p and q then store them in a list
        the first/last common parent they have is their ancestor
        """
        p_parents = []
        q_parents = []
        parents = p_parents
        def find_node(root, p, parent, p_p):
            nonlocal p_parents

            if not root:
                return False

            if root.val == p.val:
                p_parents = p_p[:] + [root.val]
                return
            
            find_node(root.left, p, root.val, p_p + [root.val])

            # p_parents.append(root.val)
            find_node(root.right, p, root.val, p_p + [root.val])
            
            # p_parents.pop()
            return 



        find_node(root, p, root.val, [])
        parents = p_parents[:]
        p_parents = q_parents
        find_node(root, q, root.val, [])
        # print(parents, p_parents )
        aset = set(p_parents)
        for idx in range(len(parents)-1, -1, -1):
            if parents[idx] in aset:
                return TreeNode(parents[idx])
        
        return TreeNode(1)
                

            




