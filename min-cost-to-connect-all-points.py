class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        manhattan distance = |xi - xj| + |yi - yj|

        [[0,0],[2,2],[3,10],[5,2],[7,0]]

        [0,0], [2,2] -> 4
        [2,2], [5,2] -> 3
        [5,2], [7,0] -> 4
        [2,2],[3,10] -> 9

        """
        def manhattan(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        parent = {}
        n = len(points)
        rank = [1] * n
        def find(x):
            if x not in parent:
                parent[x] = x
            elif parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            p_x = find(x)
            p_y = find(y)
            if p_x != p_y:
                if rank[p_x] >= rank[p_y]:
                    rank[p_x] += rank[p_y]
                    parent[p_y] = parent[p_x]
                else:
                    rank[p_y] += rank[p_x]
                    parent[p_x] = parent[p_y]
        mincost = 0
        posspath = []
        for i in range(n):
            for j in range(n):
                if i != j:
                    posspath.append((manhattan(points[i], points[j]), i, j))

        posspath.sort()
        for d, i, j in posspath:
            if find(i) != find(j):
                union(i, j)
                mincost += d
        
        return mincost