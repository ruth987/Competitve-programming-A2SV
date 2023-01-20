class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        i = len(arr) - 1
        
        while i > 0:
            while i > 0 and arr[i] - 1 == i:
                i -= 1
            
            if i == 0:
                break
            
            index = arr.index(i + 1)
            
            if index > 0: # if the max val is already at index 0, we dont need to swap
                arr[:index + 1] = reversed(arr[:index + 1])
                ans.append(index + 1)
            
            arr[:i + 1] = reversed(arr[:i + 1])
            ans.append(i + 1)
            i -= 1
        
        return ans