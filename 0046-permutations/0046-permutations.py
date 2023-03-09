class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        ln = len(nums)

        def backtrack(arr,start):
                
            if start == ln:
                res.append(arr[::])
                return
            if start > ln: return
            for i in range(start,len(nums)):
                # if nums[i] not in arr:
                nums[i], nums[start] = nums[start], nums[i]
                backtrack(arr,start + 1)
                nums[i], nums[start] = nums[start], nums[i]
                    
        backtrack(nums,0)
        return res
            
            