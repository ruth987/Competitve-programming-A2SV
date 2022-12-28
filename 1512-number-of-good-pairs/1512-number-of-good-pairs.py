class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
            counter = {}
            goodpairs = 0
            
            for num in nums:
                if num in counter:
                    goodpairs += counter[num]
                    counter[num] += 1
                else:
                    counter[num] = 1
                
            return goodpairs