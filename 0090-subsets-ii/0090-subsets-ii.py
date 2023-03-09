class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = []
        aset = set()
        nums.sort()
        
        def backtrack(nums, i, arr):
            if len(res) == 2**len(nums):
                return 
            
            if i < len(nums):
                arr.append(nums[i])
                backtrack(nums, i+1, arr)
                if tuple(arr) not in aset:
                    res.append(arr[::])
                    aset.add(tuple(arr))
                
                arr.pop()
                backtrack(nums, i+1, arr)
            
        backtrack(nums, 0, [])
        res.append([])
        return res
            
            