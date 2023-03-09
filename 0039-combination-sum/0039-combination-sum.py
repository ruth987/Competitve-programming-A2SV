class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
            
            res = []
            def backtrack(candidates, arr):
                s = sum(arr)
                if s == target:
                    res.append(arr[::])
                    return 
                 
                if s > target:
                    return 
                
                for i in range(len(candidates)):
                    arr.append(candidates[i])
                    backtrack(candidates[i:], arr)
                    arr.pop()

            backtrack(candidates, [])
            return res                
                
                
            
            
            