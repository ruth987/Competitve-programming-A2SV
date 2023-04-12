class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
          visited = set()  
        
          def dfs(isConnected, visited, i):
            if i in visited:  
                return 0
            visited.add(i) 
            for j in range(len(isConnected[i])):  
                if isConnected[i][j] == 1:
                    dfs(isConnected, visited, j) 
            return 1 
        
          provinces = 0  
          for i in range(len(isConnected)):  #
              provinces += dfs(isConnected, visited, i)  
          return provinces