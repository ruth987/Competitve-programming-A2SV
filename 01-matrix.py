class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # find the nearest zero for each cell
        rows = len(mat)
        cols = len(mat[0])
        # zeros poss
        qu = deque()
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    qu.append([r,c])
                    visited.add((r,c))

        def bfs(r,c):
            
            directions = [[1,0], [0,1], [-1,0], [0,-1]]
            distance = 0
            while qu:
                length = len(qu)

                for i in range(length):
                    row,col = qu.popleft()
                    if mat[row][col] == 1:
                        answer[row][col] = distance

                    for dr,dc in directions:
                        r,c = row+dr, col+dc

                        if r < 0 or r >= rows or c < 0 or c >= cols:
                            continue

                        if (r,c) not in visited:
                            visited.add((r,c))
                            qu.append([r,c])
                distance += 1

        answer = mat[::]
        bfs(0,0)
        
        return answer