class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = [0]*len(arr)
        
        for idx in range(len(arr)-1, -1, -1):
            if idx == len(arr)-1:
                ans[idx] = -1
            else:
                ans[idx] = max(arr[idx+1],ans[idx+1])
        
        return ans
      