"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        if not root.children:
            return 1

        max_dep = 1
        def depth(root, dep):
            nonlocal max_dep
            if not root:
                return 1
            max_dep = max(max_dep, dep)
            for node in root.children:
                depth(node, dep+1)
        depth(root, 0)
        return max_dep+1