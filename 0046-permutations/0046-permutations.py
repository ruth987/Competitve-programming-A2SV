class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        ln = len(nums)

        def backtrack(nums,arr):

            if len(arr) == ln:
                res.append(arr[::])
                return
            
            for i in range(len(nums)):
                arr.append(nums[i])
                backtrack(nums[:i] + nums[i+1:],arr)
                arr.pop()
                
        backtrack(nums, [])
        return res
            
            