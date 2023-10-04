class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        path_cost = {}
        for from_, to, time in times:
            graph[from_].append(to)
            path_cost[(from_, to)] = time

        visited = set()
        visited.add(k)
        minheap = []
        for nei in graph[k]:
            heappush(minheap, (path_cost[k, nei], nei))
        # print(minheap)
        count = 0
        while minheap:
            cost, node = heappop(minheap)
            visited.add(node)
            if len(visited) == n:
                return cost

            for nei in graph[node]:
                if nei in visited: continue
                heappush(minheap, (path_cost[(node, nei)]+cost, nei))
        
        return -1