class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        for idx in range(1,len(arr)):
            arr[idx] += arr[idx-1]
            
        arr = [0]+arr
        left, right, count = 1, k, 0
        
        while right < len(arr):
            if ((arr[right]-arr[left-1])/k) >= threshold:
                count += 1
            left+=1
            right+=1
            
        return count
                    
        