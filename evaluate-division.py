class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i, eq in enumerate(equations):
            x, y = eq
            graph[x].append([y, values[i]])
            graph[y].append([x, 1 / values[i]])
        
        print(graph)
        
        def dfs(num, deno):
            print(num, deno)
            if num == deno:
                return 1
            
            mul = 0
        
            for nei in graph[num]:
                node, val = nei
                if node not in visited:
                    visited.add(node)
                    mul += dfs(node, deno) * val

            return mul if mul >= 0 else -1
                    
        
        ans = []
        for n, d in queries:
            if n not in graph:
                ans.append(-1)
            else:
                visited = set()
                visited.add(n)
                t = dfs(n, d)
                if t == 0:
                    ans.append(-1)
                else:
                    ans.append(t)
        
        return ans