class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        neighbors = {node:set() for node in range(numCourses)}
        incomming = defaultdict(int)
        preLookup = defaultdict(set)

        for pre,aft in prerequisites:
            neighbors[pre].add(aft)
            incomming[aft] += 1
        
        qu = deque()
        for n in neighbors:
            if incomming[n] == 0:
                qu.append(n)
        
        while qu:
            cur = qu.popleft()
            for neig in neighbors[cur]:
                preLookup[neig].add(cur)
                preLookup[neig].update(preLookup[cur])

                incomming[neig] -= 1
                if incomming[neig] == 0:
                    qu.append(neig)
        
        result = [q[0] in preLookup[q[1]] for q in queries]
        return result