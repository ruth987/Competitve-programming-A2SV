class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mydict, count = {0:1}, 0
        
        for idx in range(1,len(nums)):
            nums[idx] += nums[idx-1]
            
        for number in nums:
            if number-k in mydict:
                count += mydict[number-k]
            mydict[number] = mydict.get(number, 0)+1
        return count
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
