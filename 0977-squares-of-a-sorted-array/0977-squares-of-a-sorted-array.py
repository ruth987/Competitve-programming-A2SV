class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums)-1
        answer = []
        
        while left <= right:
            if nums[left]*nums[left] > nums[right]*nums[right]:
                answer.append(nums[left]*nums[left])
                left+=1
            else:
                answer.append(nums[right]*nums[right])
                right-=1
                
        return answer[::-1]
        