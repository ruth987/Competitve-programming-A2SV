class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        num_of_rows = len(grid)
        num_of_cols = len(grid[0])
        rows_calculated = []
        cols_calculated = []
        # for each row ones count and zeros count 
        for index in range(num_of_rows):
            ones, zeros = 0, 0
            for idx in range(num_of_cols):
                if grid[index][idx] == 1:
                    ones += 1
                else:
                    zeros += 1

            rows_calculated.append([ones-zeros]*num_of_cols)

        # print(rows_calculated)
            
        # for each col ones count ans zeros count
        cols = []
        for idx in range(num_of_cols):
            ones, zeros = 0, 0
            for index in range(num_of_rows):
                if grid[index][idx] == 1:
                    ones += 1
                else:
                    zeros += 1
            cols.append(ones-zeros)
        for i in range(num_of_rows):
            cols_calculated.append(cols)
            
        # print(cols_calculated)
        for i in range(num_of_rows):
            for j in range(num_of_cols):
                grid[i][j] = rows_calculated[i][j] + cols_calculated[i][j]
        
        return grid
        
        
        
        
        
        
        