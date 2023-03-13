class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        row, col = len(board), len(board[0])
        path = set()
        def backtrack(r, c, idx):
            # basecase
            if idx == len(word):
                return True
            if r >= row or c >= col or r < 0 or c < 0 or word[idx] != board[r][c] or (r,c) in path:
                return False
            path.add((r,c))
            res = backtrack(r+1, c, idx+1) or backtrack(r, c+1, idx+1) or backtrack(r-1, c, idx+1) or backtrack(r, c-1, idx+1)
            path.remove((r,c))
            return res
             
            
             
            
        for r in range(row):
            for c in range(col):
                if backtrack(r,c,0):
                    return True
        return False
                