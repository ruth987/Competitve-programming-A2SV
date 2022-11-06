class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mydict = {0:1} #summation : count of that
        count, psum = 0, 0
        
        for number in nums:
            psum += number
            remainder = psum % k
            if remainder in mydict:
                count += mydict[remainder]
                mydict[remainder] += 1
            else:   
                mydict[remainder] = 1
        return count
            