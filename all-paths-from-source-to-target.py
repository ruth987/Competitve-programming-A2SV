class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        graphh = defaultdict(list)
        n = len(graph)
        for i in range(n):
            graphh[i] = graph[i]

        ans = []
        path = [0]
        
        def dfs(item):
            if item == n-1:
                ans.append(list(path))
                return

            for it in graphh[item]:
                path.append(it)
                dfs(it)
                path.pop()
            

        dfs(0)
        return ans