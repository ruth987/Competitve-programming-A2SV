class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n<3:
            return False
        
        pivot = max(arr)
        idx = arr.index(pivot)
        
        if idx == 0  or idx == n-1:
            return False
        for i in range(idx- 1):
            if arr[i]>= arr[i+1]:
                return False
        for j in range(idx, n-1) :
            if arr[j] <= arr[j+1]:
                return False

        return True
            

                
            