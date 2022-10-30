class NumMatrix:
        def __init__(self, matrix: List[List[int]]):
            rows, cols = len(matrix), len(matrix[0])
            self.sumMat = [[0]*(cols+1) for row in range(rows+1)]
            
            for row in range(rows):
                prefix = 0
                for col in range(cols):
                    prefix += matrix[row][col]
                    above = self.sumMat[row][col+1]
                    self.sumMat[row+1][col+1] = prefix + above
            
        def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
            row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1
            bottomRight = self.sumMat[row2][col2]
            above = self.sumMat[row1-1][col2]
            left = self.sumMat[row2][col1-1]
            topLeft = self.sumMat[row1-1][col1-1]
            
            return bottomRight-above-left+topLeft
   


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
