class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        dis =  [-1 for _ in range(n)]

        for from_, to, price in flights:
            graph[from_].append([to, price])

        dis[src] = 0
        qu = deque([src])
        count = 0
        while qu and count <= k:
            ln = len(qu)
            new_dis = list(dis)
            for i in range(ln):
                cur = qu.popleft()
                for neighbor in graph[cur]:
                    if new_dis[neighbor[0]] == -1 or new_dis[neighbor[0]] > dis[cur]+neighbor[1]:
                        new_dis[neighbor[0]] = dis[cur] + neighbor[1]
                        qu.append(neighbor[0])

            count += 1
            dis = new_dis

        return dis[dst]