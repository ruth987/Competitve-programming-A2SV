class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        if len(arr) < 3:
            return 0
        left, right = 0, 1
        up, down = 0, 0
        max_len = 0
        
        while right < len(arr):
            if arr[right]>arr[right-1] and down == 0:
                up +=1
                right +=1
            elif arr[right]>arr[right-1] and down > 0:
                max_len = max(max_len, right-left)
                up = 0
                up +=1
                down = 0
                left += 1
                right = left+1
            elif arr[right]<arr[right-1] and up == 0:
                left = right
                right+=1
            elif arr[right]<arr[right-1] and up > 0:
                down +=1
                right +=1
            #elif arr[right]==arr[right-1]:
            else:
                if up > 0 and down >0:
                    max_len = max(max_len, right-left)
                up = 0
                down = 0
                left +=1 
                right =left+1
        if up > 0 and down >0:
            max_len = max(max_len, right-left)
        return max_len
            
                
            
              
            
            