class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        
        """
        parent = {}
        def representative(x):
            if x not in  parent:
                parent[x] = x
            elif x != parent[x]:
                parent[x] = representative(parent[x]) 
            return parent[x]
        
        def union(x, y):
            n_x = representative(x)
            n_y = representative(y)

            if n_x != n_y:
                parent[n_x] = n_y
            else:
                return [x,y]
            
        for x,y in edges:
            ans = union(x, y)
            if ans:
                return ans