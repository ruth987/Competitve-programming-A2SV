class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums.sort()
        ln = len(nums)
        stack = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                stack.append(nums[i])
        
        nums = stack[:]
        
        # print("sorted", nums)
        l = 0
        r = 1
        max_len = 1
        minval = 0
        endval = 0
        while r < len(nums):
            while r < len(nums) and nums[r]-nums[l] < ln and nums[r]!=nums[r-1]:
                r += 1
            
            if r-l > max_len:
                print("l r", l, r)
                minval = l
                endval = r
                max_len = max(max_len, r-l) 

            if r < len(nums) and nums[r] == nums[r-1]:
                l = r

            l += 1
            r += 1  

        arr = nums[minval:endval]

        # print("arr",arr)
        if not arr:
            return ln-1


        rep = ln - (len(arr) - (len(arr) - len(set(arr)))) 
  
        return rep