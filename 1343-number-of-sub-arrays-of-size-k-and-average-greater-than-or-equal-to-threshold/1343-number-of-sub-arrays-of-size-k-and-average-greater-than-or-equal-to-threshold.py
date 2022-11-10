class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        for idx in range(1, len(arr)):
            arr[idx] += arr[idx-1]
        arr = [0]+arr
        
        left, count = 1, 0
        
        for right in range(k,len(arr)):
            if (arr[right]-arr[left-1])/k >= threshold:
                count += 1
            left+=1

        return count
    