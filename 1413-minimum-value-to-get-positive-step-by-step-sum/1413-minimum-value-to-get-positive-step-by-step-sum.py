class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        mins = []
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        
        for number in nums:
            if number < 1:
                mins.append(number)
        if not mins:
            return 1
        return abs(min(mins))+1
                
                