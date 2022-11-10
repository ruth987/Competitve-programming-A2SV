class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        c, j, n = 0, 0, len(arr)
        s = sum(arr[:k])
        
        if s >= k*threshold:
            c = 1
            
        for i in range(k,n):
            s += arr[i] - arr[j]
            if s >= k*threshold:
                c += 1
            j += 1
            
        return c
    