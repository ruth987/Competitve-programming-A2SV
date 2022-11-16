class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        lnums = nums[:]
        lnums.sort()
        mydict = {}
        for idx in range(len(lnums)):
            if lnums[idx] not in mydict:
                mydict[lnums[idx]] = idx
        for num in nums:
            ans.append(mydict[num])
        return ans
    