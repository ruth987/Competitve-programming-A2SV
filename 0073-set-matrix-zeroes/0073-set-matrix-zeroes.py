class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_len = len(matrix)
        col_len = len(matrix[0])
        zeros_row = set()
        zeros_col = set()
        
        for row in range(row_len):
            for col in range(col_len):
                if matrix[row][col] == 0:
                    zeros_row.add(row)
                    zeros_col.add(col)
        
        for r in range(row_len):
            for c in range(col_len):
                if r in zeros_row or c in zeros_col:
                    matrix[r][c] = 0
        
        #print(matrix)
        
        