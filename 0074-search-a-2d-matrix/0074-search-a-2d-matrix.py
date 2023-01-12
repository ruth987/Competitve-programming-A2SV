class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col_len = len(matrix[0])
        start, end = 0, (len(matrix)*col_len)-1
        
        while start <= end:
            middle = (start+end) // 2
            curr_row = middle//col_len
            curr_col = middle%col_len
            if matrix[curr_row][curr_col] == target:
                return True
            elif matrix[curr_row][curr_col] < target:
                start = middle+1
            elif matrix[curr_row][curr_col] > target:
                end = middle-1
                
        return False
    