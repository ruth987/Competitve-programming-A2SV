class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #a dictionary to store what we had before and how many times
        mydict = {0:1}
        #how many subarrays have a sum that equals k
        count = 0
        #prefix sum
        for idx in range(1,len(nums)):
            nums[idx] += nums[idx-1]
            
        for number in nums:
            #if number-k in dictionary currentnumber -(number-k) == k 
            if number-k in mydict:
                count += mydict[number-k]
            mydict[number] = mydict.get(number, 0)+1
        return count
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
