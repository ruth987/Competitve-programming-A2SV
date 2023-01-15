class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
       # change the matrix to one dimentional and just travers and store it in the new one
        row_len = len(mat)
        col_len = len(mat[0])
        size = row_len * col_len
        ans_size = r * c
        
        if ans_size < size or ans_size > size:
            return mat
        ans = [[0 for i in range(c)] for j in range(r)]
        
        for idx in range(size):
            mat_row = idx // col_len
            mat_col = idx % col_len
            ans_row = idx // c
            ans_col = idx % c
            ans[ans_row][ans_col] = mat[mat_row][mat_col]
            
        return ans
                