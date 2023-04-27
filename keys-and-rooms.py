class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # return true if i can visit all rooms else false

        """
        rooms = [0:[1],1:[2],2:[3],3:[]]
        [[1,3],[3,0,1],[2],[0]]
        3,1,0
         3 
        rooms_ = [i for i in range(len(rooms))]
        keys = deque([  ])
        if len(visited) != rooms_
        """
        def bfs():
            visited = set()
            visited.add(0)
            qu = deque()
            for r_no in rooms[0]:
                qu.append(r_no)
                visited.add(r_no)

            while qu:
                length = len(qu)
                for key in range(length):
                    room_no = qu.popleft()
                    for r_no in rooms[room_no]:
                        if r_no not in visited:
                            visited.add(r_no)
                            qu.append(r_no)
            # print(visited, len(rooms))          
            if len(visited) != len(rooms):
                return False
            return True
        
        return bfs()