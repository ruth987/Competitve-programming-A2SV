class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        return the number of all possible expressions i can build that sum up to 
        target.
        """
        mydict = {}

        def backtrack(index, total):
            if index == len(nums):
                if total == target:
                    return 1
                return 0
            if (index,total) in mydict:
                return mydict[(index, total)]
            mydict[(index, total)] = (backtrack(index+1, total+nums[index]) + 
                                    backtrack(index+1, total-nums[index]))
            return mydict[(index, total)]
        
        return backtrack(0, 0)