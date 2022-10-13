class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, 1
        count = 0
        for number in nums:
            if number == val:
                count+=1
                
        while right < len(nums):
            if nums[left] == val :
                while right< len(nums) and nums[right] == val:
                    right+=1
                if right < len(nums):
                    nums[left], nums[right] = nums[right], nums[left]
            left+=1
            right+=1

        return len(nums)-count
                
            
                