class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        [[1,0],[2,0],[3,1],[3,2]]

        """
        graph = defaultdict(list)
        incomming = [0 for _ in range(numCourses)]
        for after, pre in prerequisites:
            graph[pre].append(after)
            incomming[after] += 1
        print(graph)
        qu = deque()
        for idx in range(numCourses):
            if incomming[idx] == 0:
                qu.append(idx)
        
        c = 0
        while c < len(qu):
            x = qu[c]      
            c += 1
            for k in graph[x]:
                incomming[k] -= 1
                if incomming[k] == 0:
                    qu.append(k)
        
        return qu if numCourses==len(qu) else []