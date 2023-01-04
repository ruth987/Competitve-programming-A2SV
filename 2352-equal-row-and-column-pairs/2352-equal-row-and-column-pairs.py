class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        n = len(grid[0])
        colomons = []
        ans = 0
        
        for i in range(n):
            col = []
            for idx in range(len(grid)):
                col.append(grid[idx][i])
            colomons.append(col)
        
        for row in grid:
            for col in colomons:
                if row == col:
                    ans+=1
        
        return ans
                
            
            
            
            