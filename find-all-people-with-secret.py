class DSU:
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [1] * n

    def find(self, node):
        if self.par[node] != node:
            self.par[node] = self.find(self.par[node])
        return self.par[node]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if self.rank[px] > self.rank[py]:
            self.rank[px] += self.rank[py]
            self.par[py] = px
        else:
            self.rank[py] += self.rank[px]
            self.par[px] = py

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], first: int) -> List[int]:
        def unset_nodes(dsu, nodes):
            for node in nodes:
                if dsu.find(node) != dsu.find(first):
                    dsu.par[node] = node
                    dsu.rank[node] = 1

        dsu = DSU(n)
        dsu.union(0, first)
        meetings.sort(key=lambda meeting: meeting[2])

        prev_time, processed = None, set()

        for x, y, time in meetings:
            if prev_time != time:
                prev_time = time
                unset_nodes(dsu, processed)
                processed = set()

            dsu.union(x, y)
            processed.update([x, y])

        res = []
        for i in range(n):
            if dsu.find(i) == dsu.find(first):
                res.append(i)

        return res