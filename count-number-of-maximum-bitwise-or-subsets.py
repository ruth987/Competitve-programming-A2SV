class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        count = 0
        best = 0
        n = len(nums)
        for num in nums: 
            best |= num

        def go(index, current):
            nonlocal count
            if index == n:
                if current == best:
                    count += 1
                return
            go(index+1, current)
            go(index+1, current | nums[index])

        go(0, 0)
        return count