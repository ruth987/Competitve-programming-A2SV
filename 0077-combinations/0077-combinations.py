class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []
        
        def backtrack(n, k, i, nums):

            if len(nums) == k:
                res.append(nums[::])
                return 
            if i > n: 
                return
            nums.append(i)
            backtrack(n, k, i+1, nums)
            nums.pop()
            backtrack(n, k, i + 1,nums)
            
        backtrack(n, k, 1, [])
        return res
    