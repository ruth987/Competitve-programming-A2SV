class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        answer = []
        direction = 0
        row_len = len(matrix)
        col_len = len(matrix[0])
        # traversing pointers : top, down, left , right
        top, down = 0, row_len-1
        left, right = 0, col_len-1
        
        while top <= down and left <= right: # till there is no more to add
            # direction - 0 to the right
            if direction == 0:
                for idx in range(left, right+1):
                    answer.append(matrix[top][idx])
                top += 1
                direction = 1
                
            # direction - 1 to the bottom
            elif direction == 1:
                for idx in range(top, down+1):
                    answer.append(matrix[idx][right])
                right -= 1
                direction = 2
                
            # direction - 2 to the left
            elif direction == 2:
                for idx in range(right, left-1,-1):
                    answer.append(matrix[down][idx])
                down -= 1
                direction = 3
                
            # direction - 3 to the top
            elif direction == 3:
                for idx in range(down,top-1,-1):
                    answer.append(matrix[idx][left])
                left += 1
                direction = 0
                
        return answer
                    
                    
            
            
            