class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        first job: determine in which row it is found using binary search and checking
        the range of the row
        second job: return true if we can find it
        """
        def search(arr, key):
            left, right = 0, len(arr)-1
            while left <= right:
                mid = (left+right)//2
                if arr[mid] == key:
                    return True
                elif arr[mid] > key:
                    right = mid-1
                else:
                    left = mid+1
            return False
        
        left, right = 0, len(matrix)-1
        res = False
        for idx in range(len(matrix)):
            if target >= matrix[idx][0] and target <= matrix[idx][-1]:
                res = (search(matrix[idx], target) or res)
        
        return res