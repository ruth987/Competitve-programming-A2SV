class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mydict = {0:1} #summation : count of that
        count, res = 0, 0
        
        for number in nums:
            res += number
            remainder = res % k
            if remainder in mydict:
                count += mydict[remainder]
                mydict[remainder] += 1
            else:   
                mydict[remainder] = 1
        return count
            