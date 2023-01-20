class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        for idx in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if j != idx and nums[j] < nums[idx]:
                    count += 1
            ans.append(count)
            
        return ans