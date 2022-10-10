class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = 0
        mydict = {0:1}
        result = 0
        for number in nums:
            sums += number
            if sums-k in mydict:
                result += mydict[sums-k]
            if sums in mydict:
                mydict[sums]+=1
            else:
                mydict[sums]=1
        return result
                