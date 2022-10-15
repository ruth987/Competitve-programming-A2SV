class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        for idx in range(1, len(nums)):
            nums[idx] += nums[idx-1]
        # [1,0,0]   
        count = 0   
        mydict = {0:1}
        
        for number in nums:
            if number-k in mydict:
                count+= mydict[number-k]
            if number not in mydict:
                mydict[number] = 1
                
            else:
                mydict[number] += 1
        return count

                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
