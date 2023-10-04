class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        matrix = [[float('inf')]*numCourses for _ in range(numCourses)]

        for start,end in prerequisites:
            matrix[start][end] = 1 

        for j in range(numCourses): 
            matrix[j][j] = 0

        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses): 
                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
        ans = []
        for s, e in queries:
            if matrix[s][e] != float('inf'):
                ans.append(True)
            else:
                ans.append(False)
        return ans