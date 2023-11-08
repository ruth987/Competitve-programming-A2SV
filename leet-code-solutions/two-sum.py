class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #an even better approach
        hashmap = {}
        for idx, num in enumerate(nums):
            if target-num in hashmap:
                return [hashmap[target-num], idx]
            hashmap[num] = idx


        """
        time: O(n)
        space: O(n)
        """
        
