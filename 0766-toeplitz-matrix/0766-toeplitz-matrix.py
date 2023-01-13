class Solution(object):
    def isToeplitzMatrix(self, matrix):
        #from row highest to row lowest
        for r in range(len(matrix)-1,-1,-1):
            c = 0
            val = matrix[r][c]
            for row in range(r, len(matrix)):
                if matrix[row][c] != val:
                    return False
                c+=1
                if c >= len(matrix[0]):
                    break

        #from col lowest to col highest
        for c in range(1, len(matrix[0])):
            r = 0
            val = matrix[r][c]
            for col in range(c, len(matrix[0])):
                if matrix[r][col] != val:
                     return False
                r+=1
                if r >= len(matrix):
                    break
        return True
