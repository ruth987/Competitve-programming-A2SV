class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        """
        if the source and the destination are in the same union we can say 
        there is a path between the two nodes

        """
        parent = {}
        rank = [1] * n
        def representative(x):
            if x not in  parent:
                parent[x] = x
            elif x != parent[x]:
                parent[x] = representative(parent[x]) 
            return parent[x]
        
        def union(x, y):
            x = representative(x)
            y = representative(y)

            if rank[x] > rank[y]:
                rank[y] += rank[x]
                parent[y] = x

            elif rank[x] < rank[y]:
                rank[x] += rank[y]
                parent[x] = y

            else: # rank[x] == rank[y]
                rank[x] += 1
                parent[x] = y
            
        for x,y in edges:
            union(x, y)
        return representative(source) == representative(destination)