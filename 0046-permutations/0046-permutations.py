class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        ln = len(nums)

        def backtrack(arr):
                
            if len(arr) == ln:
                res.append(arr[::])
                return
            
            for i in range(len(nums)):
                if nums[i] not in arr:
                    arr.append(nums[i])
                    backtrack(arr)
                    arr.pop()
                    
        backtrack( [])
        return res
            
            