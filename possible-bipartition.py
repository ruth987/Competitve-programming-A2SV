class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for x,y in dislikes:
            graph[x].append(y)
            graph[y].append(x)

        group = {i:None for i in range(1, n+1)}


        def dfs(node, g):
            if not group[node]:
                group[node] = g
            else:
                return group[node]==g

            for p in graph[node]:
                if not dfs(p, 2 if g == 1 else 1):
                    return False
            return True
        
        for m in range(1, n+1):
            if not group[m] and not dfs(m,1):
                return False
        return True