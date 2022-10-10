class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        for idx in range(1, len(nums)):
            nums[idx] += nums[idx-1]
        
        mydict = {0:1}
        result = 0
        for number in nums:
            if number-k in mydict:
                result += mydict[number-k]
            if number in mydict:
                mydict[number]+=1
            else:
                mydict[number]=1
        return result
                