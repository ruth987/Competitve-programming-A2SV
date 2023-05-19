class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        """
        i can make the parent as the m
        """
        parent = {}
        def representative(x):
            if x not in parent:
                parent[x] = x
            elif x != parent[x]:
                parent[x] = representative(parent[x])
            return parent[x]
        
        def union(x, y):
            p_x = representative(x)
            p_y = representative(y)

            if p_x < p_y:
                parent[p_y] = p_x
            else:
                parent[p_x] = p_y
        
        for x,y,d in roads:
            union(x, y)
        
        min_p = float(inf)
        for x,y,d in roads:
            if representative(x) == 1:
                min_p = min(min_p, d)
        
        return min_p