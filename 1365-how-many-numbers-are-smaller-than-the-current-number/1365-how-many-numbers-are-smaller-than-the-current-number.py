class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        lnums = nums[:]
        nums.sort()
        mydict = {}
        ans = []
        
        for i in range(len(nums)):
            if nums[i] not in mydict:
                mydict[nums[i]] = i
        
        for idx in range(len(lnums)):
            ans.append(mydict[lnums[idx]])
        
        return ans
    