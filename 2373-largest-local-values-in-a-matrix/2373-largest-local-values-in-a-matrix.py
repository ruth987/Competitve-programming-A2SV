class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        # iniatialize the starting points for each
        row_start = 0
        row_end = 2
        
        # declaring the end of row and col
        row_max, col_max = len(grid), len(grid[0])
        answer = []
        
        # for each row interval we check all col intervals till col_max
        while row_end < row_max: 
            row_ans = []
            col_end, col_start = 2, 0
            
            while col_end < col_max:
                max_val = 0
                for r in range(row_start, row_start+3):
                    for c in range(col_start, col_start+3):
                        max_val = max(max_val, grid[r][c])

                row_ans.append(max_val)
                col_start+=1
                col_end+=1
                
            answer.append(row_ans)
            row_start += 1
            row_end += 1
            
        return answer
    