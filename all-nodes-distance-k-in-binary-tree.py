# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        """
        we can do this with bfs
        so the question becomes:
            all nodes at level k+1 if the initial point is the target
        how can we take the target as the initial point?
        """
        # first build the graph - PLR
        # for each node store the parent and the children as the value of the key
        graph = defaultdict(list)
        def traverse(root, parent):
            if not root:
                return 
            if parent:
                graph[root.val].append(parent.val)
            if root.left:
                graph[root.val].append(root.left.val)
                traverse(root.left, root)
            if root.right:
                graph[root.val].append(root.right.val)
                traverse(root.right, root)
        traverse(root, None)
        # now we built the graph we can do the bfs starting from the target

        qu = deque()
        qu.append(target.val)
        visited = set()
        visited.add(target.val)
        count = 0
        ans = []
        while qu:
            length = len(qu)

            for i in range(length):
                val = qu.popleft()
                if count == k:
                    ans.append(val)
                for v in graph[val]:
                    if v not in visited:
                        qu.append(v)
                        visited.add(v)
            count += 1

        return ans