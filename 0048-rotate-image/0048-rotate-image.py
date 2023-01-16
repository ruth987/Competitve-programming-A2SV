class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # transpose 
        n = len(matrix)
        for r in range(n):
            for c in range(r,n):
                temp = matrix[r][c]
                matrix[r][c] = matrix[c][r]
                matrix[c][r] = temp
                
        for row in range(n):
            left, right = 0, n-1
            while left < right:
                t = matrix[row][left]
                matrix[row][left] =  matrix[row][right]
                matrix[row][right] = t
                left += 1
                right -= 1
        print(matrix)
