class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        try to find the element that appears only once.
        we can simply solve this problem using hashmap but we arenot supposed to
        but just for now let's solve it using dictionary/ hashmap:
        """
        nums = collections.Counter(nums)
        
        for item in nums.items():
            if item[1] == 1:
                return item[0]
            