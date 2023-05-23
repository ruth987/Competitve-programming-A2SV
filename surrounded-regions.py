class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        direction=[(0,1),(1,0),(0,-1),(-1,0)]
        def dfs(i,j):
            nonlocal direction
            board[i][j]=0

            for (r,c) in direction:
                new_r=r+i
                new_c=c+j
                if  0<=new_r<m and 0<=new_c<n and board[new_r][new_c]=='O':
                    board[new_r][new_c]=0
                    dfs(new_r,new_c)

        m=len(board)
        n=len(board[0])
        for i in range(m):
            for j in range(n):
                if i==0 or i==m-1 or j==0 or j==n-1:
                    if board[i][j]=='O':
                        dfs(i,j)
        for i in range(m):
            for j in range(n):
                if board[i][j]=='O':
                    board[i][j]='X'
                elif board[i][j]==0:
                    board[i][j]='O'