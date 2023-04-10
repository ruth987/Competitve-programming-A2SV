class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u,v in edges:
            graph[v].append(u)
            graph[u].append(v)
            
        for key,val in graph.items():
            if len(val) == len(edges):
                return key