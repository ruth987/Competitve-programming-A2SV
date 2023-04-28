class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends_ = set()
        for dead in deadends:
            deadends_.add(tuple(map(int, list(dead))))

        if (0,0,0,0) in deadends_:
            return -1
            
        qu = deque()
        # append the start point
        qu.append([0,0,0,0])
        visited = set()
        visited.add((0,0,0,0))
        turns = 0
        while qu:
            # print(qu)
            length = len(qu)

            for i in range(length):
                poss = qu.popleft()
                if poss == list(map(int, list(target))):
                    return turns

                dir_ = [[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1],
                         [-1,0,0,0], [0,-1,0,0], [0,0,-1,0], [0,0,0,-1]]

                index = 0
                for dr,dc,dz,dy in dir_:
                    possible = [poss[0]+dr, poss[1]+dc, poss[2]+dz, poss[3]+dy]

                    if possible[index] == 10:
                        possible[index] = 0
                    if possible[index] == -1:
                        possible[index] = 9

                    if tuple(possible) not in visited and tuple(possible) not in deadends_:
                        qu.append(possible)
                        visited.add(tuple(possible))
                    index += 1
                    if index == 4:
                        index = 0
            turns += 1
        return -1