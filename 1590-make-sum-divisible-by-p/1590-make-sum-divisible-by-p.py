class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        """
        shortest subarray with sum equals k = total_sum % p
        
        """
        total_sum = sum(nums)
        k = total_sum%p
        if k==0:
            return 0
        if k in nums:
            return 1
        
        for idx in range(1,len(nums)):
            nums[idx] += nums[idx-1]
        # print(nums)
        for idx in range(len(nums)):
            nums[idx] = nums[idx]%p
        # print(nums)
        # nums = [0]+nums
        mydict = {0:-1}
        # print(k)
        min_len = len(nums)
        for idx in range(len(nums)):
            if nums[idx]-k in mydict :
                # print(idx, nums[idx], nums[idx]-k, mydict[nums[idx]-k])
                min_len = min(min_len, idx-mydict[nums[idx]-k])
            if nums[idx]+p-k in mydict:
                min_len = min(min_len, idx-mydict[nums[idx]+p-k])
            mydict[nums[idx]] = idx
            
        if min_len == len(nums):
            return -1
        return min_len
                
        
       