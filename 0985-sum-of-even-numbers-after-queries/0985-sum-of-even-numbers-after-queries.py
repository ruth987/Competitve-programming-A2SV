class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        answer = [] # where we store the sum of even values after each queries
        
        #know the sum of evens
        sum_ = 0
        for num in nums:
            if num%2 == 0:
                sum_ += num
                
        for que in queries:
            value = que[0]
            index = que[1]
            # if the previous val is even then get rid of it 
            if nums[index] %2 == 0:
                sum_ -= nums[index]
                
            nums[index] = nums[index] + value
            #if the new val is even add it up with the evens
            if nums[index] %2 == 0:
                sum_ += nums[index]

            answer.append(sum_)
        
        return answer