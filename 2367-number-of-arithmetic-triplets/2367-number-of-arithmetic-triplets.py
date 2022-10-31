class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        #bruteforce
        art_triplets = 0
        for number in nums:
            for num in nums:
                if num-number == diff:
                    for n in nums:
                        if n - num==diff:
                            art_triplets += 1
        return art_triplets