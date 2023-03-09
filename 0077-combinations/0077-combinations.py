class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        arr = [i for i in range(1, n+1)]
        
        
        nums = []
        res = []
        
        def backtrack(n, k, start, nums):
            # if k == len(arr):
            #     res.append(arr[::])
            #     return 
            if len(nums) == k:
                res.append(nums[::])
                return 
            
            for i in range(start, len(arr)+1):
                nums.append(i)
                backtrack(n, k, i+1, nums)
                nums.pop()
            
        backtrack(n, k, 1, [])
        return res
    