class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        # print(graph)
        seen = set()
        ans = [0]*n
        def dfs(node):
            adict = Counter()
            if node not in seen:
                adict[labels[node]] += 1
                seen.add(node)
                for nei in graph[node]:
                    adict += dfs(nei)
                ans[node] = adict[labels[node]]
            return adict


        dfs(0)
        return ans