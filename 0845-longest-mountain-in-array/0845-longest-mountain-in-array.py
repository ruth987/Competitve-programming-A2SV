class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        left, right = 0, 1
        mount_len, downs, ups = 0, 0, 0
        
        while right < len(arr):
            if arr[right]>arr[right-1] and downs == 0:
                ups += 1
                
            elif arr[right]>arr[right-1] and downs != 0:
                left = right-1
                ups = 1
                downs = 0
                
            elif arr[right]<arr[right-1] and ups != 0:
                mount_len = max(mount_len, right-left+1)
                downs+=1
                
            elif arr[right]<arr[right-1] and ups == 0:
                left = right
            else:
                left = right
                ups = downs = 0
            right+=1

        return mount_len
    