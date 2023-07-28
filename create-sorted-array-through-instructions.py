from sortedcontainers import SortedList

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        mod = 10**9+7
        nums = SortedList()
        cost = 0
        for num in instructions:
            nums.add(num)
            cost += (min(nums.bisect_left(num), len(nums)-nums.bisect_right(num)))

        return cost%mod