class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for x,y in adjacentPairs:
            graph[x].append(y)
            graph[y].append(x)
            
        # print(graph)
        
        vis = set()
        ans = []

        def dfs(node):
            if node in vis:
                return 

            vis.add(node)
            ans.append(node)
            for nei in graph[node]:
                if nei in vis: continue
                dfs(nei)


        # i can start from the one with value length one
        for key,val in graph.items():
            if len(val) == 1:
                dfs(key)
                return ans