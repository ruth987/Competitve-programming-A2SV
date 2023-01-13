class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        answer = []
        reverse = False
        # row from smallest to largest
        for r in range(len(mat)):
            store = []
            c = 0
            for row in range(r,-1,-1):
                store.append(mat[row][c])
                c+=1
                if c >= len(mat[0]):
                    break
            if r%2 != 0:
                store = store[::-1]
                reverse = True
            else:
                reverse = False      
            answer += store
            
        # colomon from smallest to largest
        for c in range(1, len(mat[0])):
            store = []
            col = c
            for row in range(len(mat)-1,-1,-1):
                store.append(mat[row][col])
                col += 1
                if col >= len(mat[0]):
                    break
            if reverse == False:
                store = store[::-1]
                reverse = True
            else:
                reverse = False
            answer += store
        return answer
            