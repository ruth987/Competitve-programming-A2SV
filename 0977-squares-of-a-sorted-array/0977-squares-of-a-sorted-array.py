class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums)-1
        answer = []
        
        while left <= right:
            ll = nums[left]*nums[left]
            rr = nums[right]*nums[right]
            if ll > rr:
                answer.append(ll)
                left+=1
            else:
                answer.append(rr)
                right-=1
                
        return answer[::-1]
        