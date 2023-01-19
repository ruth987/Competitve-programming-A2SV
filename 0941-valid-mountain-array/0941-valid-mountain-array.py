class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        
        up, down = False, False
        
        for idx in range(1, len(arr)):
            if arr[idx] > arr[idx-1] and down == False:
                up  = True
            elif arr[idx] > arr[idx-1] and down == True:
                return False
            elif arr[idx] < arr[idx-1] and up == True:
                down = True
            
            elif arr[idx] < arr[idx-1] and up == False:
                return False
            
            elif arr[idx]==arr[idx-1]:
                return False
            
        if up == True and down == True:
            return True
        
        return False
            

                
            