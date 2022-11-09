class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        if rows*cols != r*c:
            return mat
        answer, cc = [], []
        for row in mat:
            for col in row:
                cc.append(col)
                if len(cc) == c:
                    answer.append(cc)
                    cc = []
        return answer
    

