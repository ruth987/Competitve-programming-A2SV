class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        distance = lambda x1,x2,y1,y2 : sqrt((x2-x1)**2 + (y2-y1)**2 )

        # build a graph
        graph = defaultdict(list)

        for i in range(len(bombs)):
            for j in range(i+1, len(bombs)):
                d = distance(bombs[i][0], bombs[j][0], bombs[i][1], bombs[j][1])
                r = bombs[i][2]+bombs[j][2]
                r2 = abs(bombs[i][2]-bombs[j][2])
                if bombs[i][2] >= d:
                    graph[i].append(j)
                if bombs[j][2] >= d:
                    graph[j].append(i)

        count = 0
        def dfs(visited, item):
            nonlocal count
            if item in visited:
                return 
            visited.add(item)
            count += 1
            for neighbour in graph[item]:
                dfs(visited, neighbour)

        max_count = 1
        for i in range(len(bombs)):
            dfs(set(), i)
            max_count = max(max_count, count)
            count = 0
        return max_count