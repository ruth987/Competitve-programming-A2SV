class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = len(nums)-1, len(nums)
        for idx in range(len(nums)):
            if nums[idx] == 0 or nums[idx]>0:
                left, right = idx-1, idx
                break

        answer = []              
        while left > -1 and right < len(nums):
            if abs(nums[left]) > abs(nums[right]):
                answer.append(nums[right]**2)
                right+=1
            elif abs(nums[left]) < abs(nums[right]):
                answer.append(nums[left]**2)
                left-=1
            else: #if they are equal.
                answer.append(nums[left]**2)
                answer.append(nums[right]**2)
                left-=1
                right+=1
        
        while left > -1:
            answer.append(nums[left]**2)
            left-=1
            
        while right < len(nums):
            answer.append(nums[right]**2)
            right+=1
            
        return answer
        
        
        
        
        
        