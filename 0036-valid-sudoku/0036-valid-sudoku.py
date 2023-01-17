class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            aset = set()
            for col in range(9):
                val = board[row][col]
                
                if val.isdigit():
                    if val not in aset:
                        aset.add(val)
                    else: #if it is already in the set
                        return False
        # print("true for the rows")
        for col in range(9):
            aset = set()
            for row in range(9):
                val = board[row][col]
                
                if val.isdigit():
                    if val not in aset:
                        aset.add(val)
                    else: # if it is already in the set
                        return False
        # print("true for the cols")   

        row_start, row_end = 0, 2
        col_start, col_end = 0, 2
        count = 0
        for i in range(9):  
            aset = set()
            for row in range(row_start, row_end+1):
                for col in range(col_start, col_end+1):
                    val = board[row][col]
                    if val.isdigit():
                        if val not in aset:
                            aset.add(val)
                        else:
                            return False
            count += 1
            if count == 3:
                count = 0
                row_start += 3
                row_end += 3
                col_start = 0
                col_end = 2
            else:
                col_start += 3
                col_end += 3
        # print("true for 3*3 box")
        
        return True
    
                    