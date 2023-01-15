class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_len = len(matrix)
        col_len = len(matrix[0])

        for row in range(row_len):
            for col in range(col_len):
                if matrix[row][col] == 0:
                    for c in range(col_len):
                        if matrix[row][c] != 0:
                            matrix[row][c] = "#"
                        
                    for r in range(row_len):
                        if matrix[r][col] != 0:
                            matrix[r][col] = "#"
        
        for r in range(row_len):
            for c in range(col_len):
                if matrix[r][c] == "#":
                    matrix[r][c] = 0
        

        #print(matrix)
        
        