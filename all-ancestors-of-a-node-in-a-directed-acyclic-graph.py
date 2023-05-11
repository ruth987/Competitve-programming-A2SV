class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        """
        [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
        n -> number of nodes -> 8 nodes 0 to 7
        edges[i] = [fromi, toi]
        answer[i] -> list of ancestors of the ith node


        """
        incomming = [0 for _ in range(n)]
        graph = defaultdict(list)
        for fromi, toi in edges:
            incomming[toi] += 1
            graph[fromi].append(toi)
        
        qu = deque()
        for i in range(n):
            if incomming[i] == 0:
                qu.append(i)
        output =  [set() for i in range(n)]
        while qu:
            length = len(qu)
            for _ in range(length):
                node = qu.popleft()
                for nei in graph[node]:
                    # store the node it came from
                    output[nei].add(node)
                    for ancestor in output[node]:
                        output[nei].add(ancestor)

                    incomming[nei] -= 1
                    if incomming[nei] == 0:
                        qu.append(nei)
        for i in range(n):
            output[i] = sorted(list(output[i]))
        return output