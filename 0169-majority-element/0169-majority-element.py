class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mydict = collections.Counter(nums)
        mydict = sorted(mydict.items(), key = lambda item:-item[1])
        return mydict[0][0]