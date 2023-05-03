class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        """
        [["+","+",".","+"],
         [".",".",".","+"],
         ["+","+","+","."]]
        
        we are expected to find the shortest path towards the exit and the exit canot
        be the same as the entrance.
        the end is when it reach the border of the grid
         
        """
        rows = len(maze)
        cols = len(maze[0])
        qu = deque()
        qu.append(entrance)
        visited = set()
        visited.add(tuple(entrance))
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        steps = 0
        while qu:
            length = len(qu)

            for i in range(length):
                row, col = qu.popleft()
                if [row,col]!=entrance and (row == 0 or row == rows-1 or col == cols-1 or col == 0):
                    return steps
                for dr,dc in directions:
                    r, c = row+dr, col+dc

                    if r<0 or r>=rows or c<0 or c>=cols or maze[r][c]=="+" or (r,c) in visited:
                        continue
                    
                    if maze[r][c] == ".":
                        
                        qu.append([r,c]) 
                        visited.add((r,c))
            steps += 1
        
        return -1